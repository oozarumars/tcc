/*
Autor: Rafael Fontenele
Este programa calcula o valor RMS da rede a cada ciclo e detecta VTCDs;
Taxa de amostragem: 6000 [Hz];
Faz os registros da duração e menor valor de cada evento;
Filtro digital de quarta ordem implementado;
Atualização do display em tempo real.
*/
#include <driver/adc.h>
#include <esp_adc_cal.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>
#include <esp_err.h>
#include <esp_log.h>
#include <WiFi.h>
#include <Arduino.h>
#include <esp_wifi.h>
#include "time.h"
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

/* Standard variables */
const int num_leituras = 60;
volatile float voltages, leituras_validas[num_leituras];
volatile float rms_12ciclos, rms_12ciclos_c;
volatile float sum = 0., sum_c = 0.;
int c = 0;
bool stts = true, leituraIsValid = true, sttsSD;
String nome_programa = "";

/* Ajuste data */
const char* ssid       = "Fontenele";
const char* password   = "35381889";
const char* ntpServer  = "pool.ntp.org";
const long  gmtOffset_sec = -10800;
const int   daylightOffset_sec = 0;
void ajusteData();
String horarioAtual();
String nomeArquivo();
String inicioAnalise, fimAnalise;

/* TCC variables */
volatile int t_primeiro_evento = 0;
float v_ref = 220.;
int t3s = 3000, t3min = 180000;
float tDuracaoGeral = 0.;
volatile float rms = 0.;
int ev_cons = 0b000000; //IM, AM, EM, IT, AT, ET
bool inicio_interrupcao = false, inicio_elevacao = false, inicio_afundamento = false;

int matriz_eventos[12][7] = {{0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0},
                             {0, 0, 0, 0, 0, 0, 0}};
                             
String vetor_cabecalho[12] = {"    < 1,15   ", "(1,10 - 1,15]", "(0,85 - 0,90]", "(0,80 - 0,85]",
                              "(0,70 - 0,80]", "(0,60 - 0,70]", "(0,50 - 0,60]", "(0,40 - 0,50]",
                              "(0,30 - 0,40]", "(0,20 - 0,30]", "(0,10 - 0,20]", "    < 0,10   "};

String vetor_cabecalhovtcd[3] = {"Interrupção", "Afundamento", "Elevação   "};

String horarios[num_leituras];

int eventos_VTCD[3][3] = {{0, 0 ,0},
                          {0, 0 ,0},
                          {0, 0 ,0}};

/* TCC Functions */
void ani_init();
void acumular_12ciclos();
void verifica_interrupcao();
void verifica_afundamento();
void verifica_elevacao();
void finalizarPrograma();

/* Display */

#define endereco  0x27
#define colunas   16
#define linhas    2
LiquidCrystal_I2C lcd(endereco, colunas, linhas);

/* SD Functions */
void registrarSD(String tInicio, String tFinal);
void writeFile(fs::FS &fs, String path, String message);
void readFile(fs::FS &fs, const char * path);
void appendFile(fs::FS &fs, String path, String message);
String caminho;

/* Reserved variables */
esp_adc_cal_characteristics_t adc_cal;
hw_timer_t* timer = NULL;
portMUX_TYPE timerMux = portMUX_INITIALIZER_UNLOCKED;

/* FreeRTOS variables */
TaskHandle_t vTaskSamplingHandle = NULL;
TaskHandle_t vTaskCheckRMSHandle = NULL;
TaskHandle_t vTaskGetReadsHandle = NULL;
TaskHandle_t vTaskAttDisplayHandle = NULL;
TaskHandle_t vTaskSDHandle = NULL;
BaseType_t xHPTW;

/* FreeRTOS functions */
void vTaskGetReads(void* parameters);
void vTaskSampling(void* parameters);
void vTaskCheckRMS(void* parameters);
void vTaskAttDisplay(void* parameters);
void vTaskSD(void* parameters);

void IRAM_ATTR onTimer(){
  BaseType_t xHPTW = pdTRUE;

  portENTER_CRITICAL_ISR(&timerMux);
  vTaskNotifyGiveFromISR(vTaskSamplingHandle, 0);
  portEXIT_CRITICAL_ISR(&timerMux);

  if(xHPTW == pdTRUE){
    portYIELD_FROM_ISR();
  }

}

void setup(){
  Serial.begin(115200);
  /*adc*/
  pinMode(GPIO_NUM_35, INPUT);
  adc1_config_width(ADC_WIDTH_BIT_12);
  adc1_config_channel_atten(ADC1_CHANNEL_7, ADC_ATTEN_DB_11);
  esp_adc_cal_value_t adc_type = esp_adc_cal_characterize(ADC_UNIT_1, ADC_ATTEN_DB_11, ADC_WIDTH_BIT_12, 1100, &adc_cal);
  if (adc_type == ESP_ADC_CAL_VAL_EFUSE_VREF) {Serial.println("eFuse Vref");}
  pinMode(2, OUTPUT);
  /*cartão SD*/
  SD.begin();
  while(!SD.begin()){
    Serial.println("Tentando abrir o cartão de memória...");
    delay(1500);
  }
  if(!SD.begin()){
    Serial.println("Card Mount Failed");
    return;
  }else{
    Serial.println("Cartão SD aberto com sucesso.");
    for(int i = 0; i < 40; i++){
      digitalWrite(2, !digitalRead(2));
      delay(100);
    }
    sttsSD = true;
  }

  /*timer*/
  timer = timerBegin(0, 8, true);
  timerAttachInterrupt(timer, &onTimer, true);
  timerAlarmWrite(timer, 1666.66667, true);
  
  /*tasks*/
  xTaskCreatePinnedToCore(vTaskSampling, "Task Sampling Data", configMINIMAL_STACK_SIZE + 1024, NULL, 3, &vTaskSamplingHandle, PRO_CPU_NUM);
  xTaskCreatePinnedToCore(vTaskCheckRMS, "Task Check RMS", configMINIMAL_STACK_SIZE + 1024, NULL, 2, &vTaskCheckRMSHandle, APP_CPU_NUM);
  xTaskCreatePinnedToCore(vTaskGetReads, "Task Get Reads", configMINIMAL_STACK_SIZE + 2048, NULL, 2, &vTaskGetReadsHandle, APP_CPU_NUM);
  xTaskCreatePinnedToCore(vTaskAttDisplay, "Task Att Display", configMINIMAL_STACK_SIZE + 2048, NULL, 1, &vTaskAttDisplayHandle, APP_CPU_NUM);
  xTaskCreatePinnedToCore(vTaskSD, "Task SD", configMINIMAL_STACK_SIZE + 2048, NULL, 1, &vTaskSDHandle, APP_CPU_NUM);
  
  /*interrupção*/
  pinMode(12, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(12), finalizarPrograma, FALLING);

  /*data*/
  ajusteData();
  inicioAnalise = horarioAtual();
  Serial.println("Programa iniciado em " + inicioAnalise);
  timerAlarmEnable(timer);
  caminho = nomeArquivo();
  Serial.println("Nome do arquivo: " + caminho);
  vTaskDelay(3000);
  digitalWrite(2, LOW);
}
 
void loop(){
  vTaskDelay(pdMS_TO_TICKS(portMAX_DELAY)); 
}

/* TASKS */

void vTaskSampling(void* parameters){
  vTaskDelay(pdMS_TO_TICKS(1000));
  /*volatile float vFiltro = 0., vAntes = 0.;*/
  volatile static float y[5] = {0., 0., 0., 0., 0.}; 
  static float u[5] = {0., 0., 0., 0., 0.};
  while(1){
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    voltages = (float(esp_adc_cal_raw_to_voltage(adc1_get_raw(ADC1_CHANNEL_7), &adc_cal))-1668.0)*0.611;
    /*Filtro de primeira ordem
    vFiltro = 0.17317*(voltages+vAntes)+0.65365*vFiltro;
    vAntes = voltages;
    sum += vFiltro*vFiltro;
    */

    /*Filtro de ordem 4*/
    for(int k = 4; k > 0; k--){
      y[k] = y[k-1];
      u[k] = u[k-1];
    }
    u[0] = voltages;
    y[0] = (7847.31 * y[1] - 9541.19 * y[2] + 5226.46 * y[3] - 1085.8 * y[4] + u[0] + 4*u[1] + 6*u[2] + 4*u[3] + u[4])/(2462.74);
    
    sum += y[0]*y[0];

    c++;

    if(c == 100){
      c = 0;
      sum_c = sum;
      xTaskNotifyGive(vTaskCheckRMSHandle);
      sum = 0.;
    }
  }
}

void vTaskCheckRMS(void* parameters){
  vTaskDelay(pdMS_TO_TICKS(1000));
  while(1){
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    rms = sqrt(sum_c*1E-2);
    acumular_12ciclos();
    verifica_interrupcao();
    verifica_afundamento();
    verifica_elevacao();
  }
}

int count_leituras = 0;
float rms_get12reads = 0.;
String dataEventoInicio = "";
void vTaskGetReads(void* parameters){ 
  vTaskDelay(pdMS_TO_TICKS(20));
  static float rms_leitura = 0., nlp = 0., nlc = 0.;
  static int count = 0, count_leituras_expurgadas = 0;
  for(;;){
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    rms_get12reads = sqrt((0.083333333)*rms_12ciclos_c);
    rms_leitura += rms_get12reads*rms_get12reads;
    count++;

    if(count == 1){
      dataEventoInicio = horarioAtual();
      Serial.println("Iniciando nova leitura...");
    }else if(count == 3000){
      if(inicio_afundamento && (tDuracaoGeral > t3s && tDuracaoGeral <= t3min)){
        leituraIsValid = false;
      }else if(inicio_interrupcao && tDuracaoGeral > t3s){
        leituraIsValid = false;
      }else if(inicio_elevacao && tDuracaoGeral > t3s){
        leituraIsValid = false;
      }

      rms_leitura = sqrt((3.3333E-4)*rms_leitura);
      String dataEventoFinal = horarioAtual();
      if(leituraIsValid){
        leituras_validas[count_leituras]=rms_leitura;
        horarios[count_leituras] = dataEventoInicio;
        count_leituras++;
        Serial.print("Leitura válida: " + String(rms_leitura) + " [V]");
      }else{
        Serial.print("Leitura expurgada: " + String(rms_leitura) + " [V]");
        count_leituras_expurgadas++;
      }
      Serial.print(" - Inicio: " + dataEventoInicio);
      Serial.println(" <-> Final: " + dataEventoFinal);
      rms_leitura = 0.;
      rms_get12reads = 0.;
      leituraIsValid = true;
      count = -1;
      xTaskNotifyGive(vTaskSDHandle);
      }
    if(count_leituras == num_leituras){
      timerAlarmDisable(timer);
      timerStop(timer);
      vTaskSuspend(vTaskCheckRMSHandle);
      vTaskSuspend(vTaskSamplingHandle);
      fimAnalise = horarioAtual();
      Serial.println("Análise finalizada.");
      Serial.println("Início: " + inicioAnalise);
      Serial.println("Fim:    " + fimAnalise);
      Serial.println("Leituras válidas: " + String(count_leituras));
      Serial.println("Leituras expurgadas: " + String(count_leituras_expurgadas));
      Serial.println("Calculando DRP e DRC...");
      xTaskNotifyGive(vTaskSDHandle);
      for(int z = 0; z < num_leituras; z++){
        if((leituras_validas[z] >= 0.87*v_ref && leituras_validas[z] < 0.92*v_ref) || (leituras_validas[z] > 1.05*v_ref && leituras_validas[z] <= 1.06*v_ref)){
          nlp++;
        }else if(leituras_validas[z] < 0.87*v_ref || leituras_validas[z] > 1.06*v_ref){
          nlc++;
        }     
      }
      Serial.println("DRC: " + String(nlc/float(num_leituras)));
      Serial.println("DRP: " + String(nlp/float(num_leituras)));
      finalizarPrograma();      
      vTaskSuspend(vTaskGetReadsHandle);
    }
  }
}

void vTaskAttDisplay(void* parameters){
  static int countVTCD = 0;
  static String cartao;
  while(1){
    countVTCD = 0;
    lcd.init(); 
    lcd.backlight();
    lcd.clear();
    for(int k = 0; k < 3; k++){
      for(int j = 0; j < 3; j++){
        countVTCD += eventos_VTCD[k][j];
      }
    }
    sttsSD==true?cartao="OK":cartao="ER";
    lcd.print("VTCDs:" + String(countVTCD));
    lcd.setCursor(10, 0);
    lcd.print("SD:" + cartao);
    lcd.setCursor(0, 1);
    lcd.print("LV:" + String(count_leituras));
    lcd.setCursor(7, 1);
    lcd.print("- " + String(rms_get12reads) + "V");
    vTaskDelay(pdMS_TO_TICKS(10000));
    //lcd.noBacklight();
    //vTaskDelay(pdMS_TO_TICKS(30000));

  }
}

void vTaskSD(void* parameters){
  static int x = 0;
  while(1){
    ulTaskNotifyTake(pdTRUE, portMAX_DELAY);
    /*if(x == 0){
      vTaskDelay(10000);
      x++;
    }*/
    writeFile(SD, "/" + caminho + ".csv", "Início do evento;Leitura;Tensao V1;VTCDS/LD;Momentaneo;Temporario;Longa;Inicio da medicao;Fim da medicao\n");
    appendFile(SD, "/" + caminho + ".csv", horarios[0] + ";1;"+String(leituras_validas[0])+";Elevacao;"+String(eventos_VTCD[2][0])+";"
      +String(eventos_VTCD[2][1])+";"+String(eventos_VTCD[2][2])+";"+inicioAnalise+";"+fimAnalise+"\n");
    appendFile(SD, "/" + caminho + ".csv", horarios[1] +  ";2;"+(num_leituras>=2?String(leituras_validas[1]):"0.00")+";Afundamento;"+String(eventos_VTCD[1][0])+";"
      +String(eventos_VTCD[1][1])+";"+String(eventos_VTCD[1][2])+"\n");
    appendFile(SD, "/" + caminho + ".csv", horarios[2] +  ";3;"+(num_leituras>=3?String(leituras_validas[2]):"0.00")+";Interrupcao;"+String(eventos_VTCD[0][0])+";"
      +String(eventos_VTCD[0][1])+";"+String(eventos_VTCD[0][2])+"\n");
    for(int i = 3; i < num_leituras; i++){
      appendFile(SD, "/" + caminho + ".csv", horarios[i] +  ";"+String(i+1)+";"+String(leituras_validas[i])+"\n");
    }
    for(int i = 0; i < 40; i++){
      digitalWrite(2, !digitalRead(2));
      delay(100);
    }
    //vTaskDelay(pdMS_TO_TICKS(50000));
  }
}

/* FUNÇÕES DE APOIO */

void acumular_12ciclos(){
  static int k = 0;
  rms_12ciclos += rms*rms;
  k++;
  if(k == 12){
    k=0;
    rms_12ciclos_c = rms_12ciclos;
    xTaskNotifyGive(vTaskGetReadsHandle);
    rms_12ciclos = 0.;
  }
}

void verifica_interrupcao(){
  static unsigned long t_i = 0, t_duracao = 0;

  if(rms < 0.1*v_ref && inicio_interrupcao == false){
      t_i = millis();
      inicio_interrupcao = true;
  }
  else if((rms >= 0.1*v_ref && inicio_interrupcao == true)){
    inicio_interrupcao = false;
    t_duracao = millis() - t_i;
    if(t_duracao <= t3s && t_duracao > 17){
      if((ev_cons&(1<<5)) == 0b0){
        eventos_VTCD[0][0]++;
        ev_cons = (1<<5);
        t_primeiro_evento = millis() - t_duracao;
        leituraIsValid = false;
        Serial.println("Interrupção momentânea("  + String(t_duracao) + " [ms]): " + String(eventos_VTCD[0][0]));
      }
    }else if(t_duracao < t3min){
      if((ev_cons&(1<<2)) == 0b0){
        eventos_VTCD[0][1]++;
        ev_cons = (1<<2);
        t_primeiro_evento = millis() - t_duracao;
        leituraIsValid = false;
        Serial.println("Interrupção temporária("  + String(t_duracao) + " [ms]): " + String(eventos_VTCD[0][1]));
      }
    }else{
      eventos_VTCD[0][2]++;
      Serial.println("Interrupção de longa duração(" + String(t_duracao) + " [ms]): " +  String(eventos_VTCD[0][2]));
      leituraIsValid = false;
    }
    ((millis() - t_primeiro_evento) > t3min)?ev_cons=0b0:pdPASS;
  }

  if(inicio_interrupcao){
    tDuracaoGeral = millis() - t_i;
  }
}

void verifica_afundamento(){
  static unsigned long t_i = 0, t_duracao = 0;
  static float menor_rms;
  if((rms >= 0.1*v_ref && rms < 0.9*v_ref) && inicio_afundamento == false){
    t_i = millis();
    inicio_afundamento = true;
    menor_rms = rms;
  }
  else if(((rms < 0.1*v_ref || rms >= 0.9*v_ref) && inicio_afundamento == true)){
    inicio_afundamento = false;
    t_duracao = millis() - t_i;
    if(t_duracao <= t3s && t_duracao > 17){
      if((ev_cons&(1<<4)) == 0b0){
        eventos_VTCD[1][0]++;
        ev_cons = (1<<4);
        t_primeiro_evento = millis() - t_duracao;
        Serial.println("Afundamento momentâneo(" + String(t_duracao) + " [ms]): " + String(eventos_VTCD[1][0]));
      }
    }else if(t_duracao > t3s && t_duracao < t3min){
      if((ev_cons&(1<<1)) == 0b0){
        eventos_VTCD[1][1]++;
        ev_cons = (1<<1);
        t_primeiro_evento = millis() - t_duracao;
        leituraIsValid = false;
        Serial.println("Afundamento temporário("  + String(t_duracao) + " [ms]): " + String(eventos_VTCD[1][1]));
      }
    }else if(t_duracao >= t3min){
      eventos_VTCD[1][2]++;
      Serial.println("Afundamento de longa duração(" + String(t_duracao) + " [ms]): " + String(eventos_VTCD[1][2]));
    }
    ((millis() - t_primeiro_evento) > t3min)?ev_cons=0b0:pdPASS;
  }
  if(rms >= 0.1*v_ref && rms < 0.9*v_ref){
    (rms<menor_rms)?menor_rms=rms:pdPASS;
  }

  if(inicio_afundamento){
    tDuracaoGeral = millis() - t_i;
  }
}

void verifica_elevacao(){
  static unsigned long t_i = 0, t_duracao = 0;
  static float maior_rms;
  if(rms > 1.1*v_ref && inicio_elevacao == false){
    t_i = millis();
    inicio_elevacao = true;
    maior_rms = rms;
  }
  if(rms > 1.1*v_ref){
    (rms>maior_rms)?maior_rms=rms:pdPASS;
  }
  else if((rms <= 1.1*v_ref && inicio_elevacao == true)){
    inicio_elevacao = false;
    t_duracao = millis() - t_i;
    if(t_duracao <= t3s && t_duracao >= 100){
      if((ev_cons&(1<<3)) == 0b0){
        eventos_VTCD[2][0]++;
        ev_cons = (1<<3);
        leituraIsValid = false;
        t_primeiro_evento = millis() - t_duracao;
        Serial.println("Elevação momentânea(" + String(t_duracao) + " [ms]): "  + String(eventos_VTCD[2][0]));
      }
    }else if(t_duracao > t3s && t_duracao < t3min){
      if((ev_cons&(1<<0)) == 0b0){
        eventos_VTCD[2][1]++;
        ev_cons = (1<<0);
        t_primeiro_evento = millis() - t_duracao;
        Serial.println("Elevação temporária(" + String(t_duracao) + " [ms]): "  + String(eventos_VTCD[2][1]));
        leituraIsValid = false;
      }
    }else if(t_duracao >= t3min){
      eventos_VTCD[2][2]++;
      Serial.println("Elevação de longa duração(" + String(t_duracao) + " [ms]): "  + String(eventos_VTCD[2][2]));
    }
    ((millis() - t_primeiro_evento) > t3min)?ev_cons=0b0:pdPASS;
  }

  if(inicio_elevacao){
    tDuracaoGeral = millis() - t_i;
  }
}

void ani_init(){
  pinMode(GPIO_NUM_2, OUTPUT);
  Serial.print("Inicializando o programa");
  digitalWrite(GPIO_NUM_2, 1);
  for(int i = 0; i < 5; i++){
    Serial.print(".");
    delay(800);
  } 
  digitalWrite(GPIO_NUM_2, 0);
  Serial.println("");
}

void ajusteData(){
  Serial.print("Conectando na rede ");
  Serial.print(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  if(WiFi.status() == WL_CONNECTED){
    digitalWrite(2, HIGH);
  }
  Serial.println("");
  Serial.println("Dispositivo conectado ao WiFi.");
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  horarioAtual();
  WiFi.disconnect(true);
  WiFi.mode(WIFI_OFF);
}

String horarioAtual(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    return "Horário não obtido.";
  }
  char timeDay[50];
  strftime(timeDay, 50, "%d/%m/%y, %a, %T", &timeinfo);
  
  return String(timeDay);
}

String nomeArquivo(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    return "Horário não obtido.";
  }
  char timeDay[50];
  strftime(timeDay, 50, "%H%M%S%d", &timeinfo);
  
  return String(timeDay);
}

void finalizarPrograma(){
  Serial.println("");
  Serial.println("| Evento | Momentâneo | Temporário | Longa Duração |");
  for(int i = 0; i < 3; i++){
    Serial.print("| " + vetor_cabecalhovtcd[i] + " |");
    for(int k = 0; k < 3; k++){
      Serial.printf("     %i    |", eventos_VTCD[i][k]);
    }
    Serial.println();
  }

  //-------------------------//
  /*
  Serial.println("");
  Serial.println("| Amplitude(pu) | I1 | I2 | I3 | I4 | I5 | I6 | I7 |");
  for(int i = 0; i < 12; i++){
    Serial.print("| " + vetor_cabecalho[i] + " |");
    for(int j = 0; j < 7; j++){
      if(matriz_eventos[i][j]<10){
        Serial.printf(" %i  |", matriz_eventos[i][j]);
      }else{Serial.printf(" %i |", matriz_eventos[i][j]);}
    }
    Serial.println();
  }
  */
}

/* FUNÇÕES CARTÃO SD */

void readFile(fs::FS &fs, const char * path){
  Serial.printf("Reading file: %s\n", path);
  File file = fs.open(path);
  if(!file){
    Serial.println("Failed to open file for reading");
    return;
  }
  Serial.println("Read from file: ");
  while(file.available()){
    Serial.write(file.read());
  }
  file.close();
}

void writeFile(fs::FS &fs, String path, String message){
  File file = fs.open(path, FILE_WRITE);
  if(!file){
    Serial.println("Failed to open file for writing");
    sttsSD = false;
    return;
  }
  if(file.print(message)){
    sttsSD = true;
  }else{
    sttsSD = false;
  }
  file.close();
}

void appendFile(fs::FS &fs, String path, String message){
  File file = fs.open(path, FILE_APPEND);
  if(!file){
    sttsSD = false;
    return;
  }
  if(file.print(message)){
    sttsSD = true;
  }else{
    sttsSD = false;
  }
  file.close();
}
