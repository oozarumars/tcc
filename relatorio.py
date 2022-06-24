from tokenize import String
import pandas as pd
import matplotlib.pyplot as plt
import os

endereco = ""
endereco_salvar = ""
opcao_formato = 0 #0 txt ou csv 1 xlsx
qtd_fases = 1
qtd_leituras = 1008
inicio_medicao = ""
final_medicao = ""

#ordem [momentaneo, temporario, longa duração]
elev = [0,0,0]
afun = [0,0,0]
interrup = [0,0,0]
interrupa = [0,0,0]
interrupb = [0,0,0]
interrupc = [0,0,0]
drp_fasea = 0
drc_fasea = 0
drp_faseb = 0
drc_faseb = 0
drp_fasec = 0
drc_fasec = 0
max_drp = 0
max_drc = 0
f1_maior = 0
f2_maior = 0
f3_maior = 0
f1_menor = 0
f2_menor = 0
f3_menor = 0


def executar():
    if opcao_formato == 0:
        dados = pd.read_csv(endereco, delimiter = ";")
    else:
        dados = pd.read_excel(endereco)

    #textos para o PDF (caso sua planilha só tenha as LV pode apagar essas linhas até o próximo #)
    global inicio_medicao, final_medicao, elev, afun, interrup, interrupa, interrup, interrupc
    inicio_medicao = dados["Inicio da medicao"][0]
    final_medicao = dados["Fim da medicao"][0]
    elev[2] = dados["Longa"][0]
    elev[1] = dados["Temporario"][0]
    elev[0] = dados["Momentaneo"][0]
    afun[2] = dados["Longa"][1]
    afun[1] = dados["Temporario"][1]
    afun[0] = dados["Momentaneo"][1]
    interrup[2] = dados["Longa"][2]
    interrup[1] = dados["Temporario"][2]
    interrup[0] = dados["Momentaneo"][2]
    if qtd_fases == 2:
        interrupa[2] = dados["Longa"][3]
        interrupa[1] = dados["Temporario"][3]
        interrupa[0] = dados["Momentaneo"][3]
        interrupb[2] = dados["Longa"][4]
        interrupb[1] = dados["Temporario"][4]
        interrupb[0] = dados["Momentaneo"][4]
    elif qtd_fases == 3:
        interrupa[2] = dados["Longa"][3]
        interrupa[1] = dados["Temporario"][3]
        interrupa[0] = dados["Momentaneo"][3]
        interrupb[2] = dados["Longa"][4]
        interrupb[1] = dados["Temporario"][4]
        interrupb[0] = dados["Momentaneo"][4]
        interrupc[2] = dados["Longa"][5]
        interrupc[1] = dados["Temporario"][5]
        interrupc[0] = dados["Momentaneo"][5]
    #

    class fase():
        tensao_ref = 220
        ltpi = 189.0
        ltai = 201.0
        ltas = 231.0
        ltps = 233.0

        def __init__(self, k):
            try:
                self.dados_rms = list(dados[f"Tensao V{k}                "])
            except:
                self.dados_rms = list(dados[f"Tensao V{k}"])

            if k == 1:
                self.titulo = "Fase A"
            elif k == 2:
                self.titulo = "Fase B"
            elif k == 3:
                self.titulo = "Fase C"
            
            for i in range(len(dados)):
                if(type(self.dados_rms[i]) != float):
                    try:
                        self.dados_rms[i] = self.dados_rms[i].replace(" V                ", "")
                    except:
                        self.dados_rms[i] = self.dados_rms[i].replace("V", "")
                    else:
                        pass
                
                    try:
                        self.dados_rms[i] = self.dados_rms[i].replace(",", ".")
                    except:
                        pass # linha

                self.dados_rms[i] = float(self.dados_rms[i])
                if(i == 0):
                    self.maiorvalorlido = self.dados_rms[i]
                    self.menorvalorlido = self.dados_rms[i]
                
                if self.dados_rms[i] < self.menorvalorlido:
                    self.menorvalorlido = self.dados_rms[i]
                if self.dados_rms[i] > self.maiorvalorlido:
                    self.maiorvalorlido = self.dados_rms[i]

        def calcular_drp(self):
            n = 0
            for j in range(len(self.dados_rms)):
                if fase.ltpi <= self.dados_rms[j] <= fase.ltai or fase.ltas <= self.dados_rms[j] <= fase.ltps:
                    n += 1
            return round((n/len(self.dados_rms))*100, 2) ##antes era 1008

        def calcular_drc(self):
            n = 0
            for j in range(len(self.dados_rms)):
                if 0 <= self.dados_rms[j] < fase.ltpi or fase.ltps < self.dados_rms[j]:
                    n += 1
            return round((n/len(self.dados_rms))*100, 2)

        def mostrar_drp(self):
            print(f"DRP da {self.titulo}: {self.calcular_drp()}%")

        def mostrar_drc(self):
            print(f"DRP da {self.titulo}: {self.calcular_drc()}%")

        def dados_histograma(self):
            k = 0.80
            for i in range(40):
                if i == 0:
                    self.dici = {"< 0.80": 0}
                self.dici[f"{round(k,2)} - {round(k+0.01,2)}"] = 0
                k += 0.01
                if i == 39:
                    self.dici["> 1.20"] = 0

            lim1 = 0.80
            lim2 = 0.81
            for j in range(40):
                for k in range(len(self.dados_rms)):
                    if lim1 <= self.dados_rms[k]/220 < lim2:
                        self.dici[f"{round(lim1,2)} - {round(lim2, 2)}"] += 1
                lim1 += 0.01
                lim2 += 0.01
            return self.dici

    class relatorio():
        def __init__(self, f1 = "" , f2 = "", f3 = ""):
            self.title = "Avaliacao de Qualidade de Energia"
            if qtd_fases == 3 or qtd_fases == 2 or qtd_fases == 1:
                self.f1 = f1
            if qtd_fases == 2 or qtd_fases == 3:
                self.f2 = f2
            if qtd_fases == 3:
                self.f3 = f3

        def graf_trp(self):
            leitura = []
            for i in range(qtd_leituras):
                leitura.append(i+1)
            
            if qtd_fases == 1:
                plt.plot(leitura, self.f1.dados_rms[0:qtd_leituras], label = "FASE A")
            if qtd_fases == 2 or qtd_fases == 3:
                plt.plot(leitura, self.f1.dados_rms[0:qtd_leituras], label = "FASE A")
                plt.plot(leitura, self.f2.dados_rms[0:qtd_leituras], label = "FASE B")
            if qtd_fases == 3:
                plt.plot(leitura, self.f3.dados_rms[0:qtd_leituras], label = "FASE C")

            plt.ylabel("Tensão [V]")
            plt.xlabel(f"Leitura [{qtd_leituras} leituras]")
            plt.fill_between(leitura, [fase.ltas]*(qtd_leituras), [fase.ltps]*(qtd_leituras), alpha = 0.3, color = "green", label = "Precária")
            plt.fill_between(leitura, [fase.ltpi]*(qtd_leituras), [fase.ltai]*(qtd_leituras), alpha = 0.3, color = "green")
            plt.fill_between(leitura, [fase.ltps]*(qtd_leituras), [235]*(qtd_leituras), alpha = 0.3, color = "orange", label = "Crítica")
            plt.fill_between(leitura, [187]*(qtd_leituras), [fase.ltpi]*(qtd_leituras), alpha = 0.3, color = "orange")
            plt.legend(ncol = 5, columnspacing = 0.2, fontsize = 10, loc = 'upper center')
            plt.grid()
            plt.xlim(1, qtd_leituras)
            plt.ylim(188, 235)
            plt.title("Tensão em Regime Permanente")
            if endereco_salvar == "":
                plt.savefig('graficotensao.png', format='png')
            else:
                plt.savefig(endereco_salvar + '/graficotensao.png', format='png')
            plt.close()

        def graf_histograma(self):
            chaves = list(self.f1.dados_histograma().keys())
            valoresfase1 = list(self.f1.dados_histograma().values())
            if qtd_fases == 2 or qtd_fases == 3:
                valoresfase2 = list(self.f2.dados_histograma().values())
            if qtd_fases == 3:    
                valoresfase3 = list(self.f3.dados_histograma().values())
            
            fig, axis = plt.subplots(qtd_fases, 1, figsize = (7,7))

            if qtd_fases == 1:
                axis.bar(chaves, valoresfase1, label = "FASE A", color = "blue")
                axis.set_ylim(0, max(valoresfase1))
                axis.fill_between([0, 6.5], max(valoresfase1), label = "FAIXA CRÍTICA", alpha = 0.7, color = "orange")
                axis.fill_between([26.5, 42], max(valoresfase1), alpha = 0.7, color = "orange")
                axis.fill_between([6.5, 11.8], max(valoresfase1), label = "FAIXA PRECÁRIA", alpha = 0.3, color = "yellow")
                axis.fill_between([25.5, 26.5], max(valoresfase1), alpha = 0.3, color = "yellow")
                axis.set_title("Histograma FASE A", size = 10, weight = "bold")
            
            if qtd_fases == 2 or qtd_fases == 3:
                axis[0].bar(chaves, valoresfase1, label = "FASE A", color = "blue")
                axis[0].set_ylim(0, max(valoresfase1))
                axis[1].bar(chaves, valoresfase2, label = "FASE B", color = "red")
                axis[1].set_ylim(0, max(valoresfase2))
                axis[0].fill_between([0, 6.5], max(valoresfase1), label = "FAIXA CRÍTICA", alpha = 0.7, color = "orange")
                axis[0].fill_between([26.5, 42], max(valoresfase1), alpha = 0.7, color = "orange")
                axis[1].fill_between([0, 6.5], max(valoresfase2), alpha = 0.7, color = "orange")
                axis[1].fill_between([26.5, 42], max(valoresfase2), alpha = 0.7, color = "orange")
                axis[0].fill_between([6.5, 11.8], max(valoresfase1), label = "FAIXA PRECÁRIA", alpha = 0.3, color = "yellow")
                axis[0].fill_between([25.5, 26.5], max(valoresfase1), alpha = 0.3, color = "yellow")
                axis[1].fill_between([6.5, 11.8], max(valoresfase2), alpha = 0.3, color = "yellow")
                axis[1].fill_between([25.5, 26.5], max(valoresfase2), alpha = 0.3, color = "yellow")
                axis[0].set_title("Histograma FASE A", size = 10, weight = "bold")
                axis[1].set_title("Histograma FASE B", size = 10, weight = "bold")

            if qtd_fases == 3:
                axis[2].bar(chaves, valoresfase3, label = "FASE C", color = "black")
                axis[2].set_ylim(0, max(valoresfase3))
                axis[2].fill_between([0, 6.5], max(valoresfase3), alpha = 0.7, color = "orange")
                axis[2].fill_between([26.5, 42], max(valoresfase3), alpha = 0.7, color = "orange")
                axis[2].fill_between([6.5, 11.8], max(valoresfase3), alpha = 0.3, color = "yellow")
                axis[2].fill_between([25.5, 26.5], max(valoresfase3), alpha = 0.3, color = "yellow")
                axis[2].set_title("Histograma FASE C", size = 10, weight = "bold")

            if qtd_fases == 1:
                axis.set_xticklabels(labels = chaves , rotation=90, size = 6)
                axis.set_xlabel("Faixa", size = 8)
                axis.set_xlim(0, 42)
            elif qtd_fases == 2 or qtd_fases == 3:
                for label in axis:
                    label.set_xticklabels(labels = chaves , rotation=90, size = 6)
                    label.set_xlabel("Faixa", size = 8)
                    label.set_xlim(0, 42)

            plt.subplots_adjust(hspace = 1)

            fig.legend(ncol = 5, columnspacing = 0.2, fontsize = 10, loc = 'upper center')
            if endereco_salvar == "":
                plt.savefig('histograma.png', format='png')
            else:
                plt.savefig(endereco_salvar + '/histograma.png', format='png')

            plt.close()

        def maior_drp(self):
            self.drp = 0.0
            self.lista_drp = []
            if qtd_fases == 1 or qtd_fases == 2 or qtd_fases == 3:
                self.lista_drp.append(self.f1)
            if qtd_fases == 2 or qtd_fases == 3:
                self.lista_drp.append(self.f2)
            if qtd_fases == 3:
                self.lista_drp.append(self.f3)

            for self.fase in (self.lista_drp):
                if self.fase.calcular_drp() > self.drp:
                    self.drp = self.fase.calcular_drp()
            return self.drp

        def maior_drc(self):
            self.drc = 0
            self.lista_drc = []
            if qtd_fases == 1 or qtd_fases == 2 or qtd_fases == 3:
                self.lista_drc.append(self.f1)
            if qtd_fases == 2 or qtd_fases == 3:
                self.lista_drc.append(self.f2)
            if qtd_fases == 3:
                self.lista_drc.append(self.f3)

            for self.fase in (self.lista_drc):
                if self.fase.calcular_drc() > self.drc:
                    self.drc = self.fase.calcular_drc()
            return self.drc       

        def gerar_relatorio(self):
            try:
                os.remove("relatorio.txt")
            except:
                pass
            if endereco_salvar == "":
                a = open("relatorio.txt", "w")
            else:
                a = open(endereco_salvar + "/relatorio.txt", "w")                   
            
            a.writelines(self.title)
            a.writelines("\n\nMaior valor lido:          Menor valor lido:")
            a.writelines(f"\n{self.f1.titulo}: {self.f1.maiorvalorlido} [V]        {self.f1.titulo}: {self.f1.menorvalorlido} [V]")
            if qtd_fases == 2 or qtd_fases == 3:
                a.writelines(f"\n{self.f2.titulo}: {self.f2.maiorvalorlido} [V]        {self.f2.titulo}: {self.f2.menorvalorlido} [V]")
            if qtd_fases == 3:
                a.writelines(f"\n{self.f3.titulo}: {self.f3.maiorvalorlido} [V]        {self.f3.titulo}: {self.f3.menorvalorlido} [V]")
            a.writelines(f"\n\nIndice de conformidade de tensao:")

            if qtd_fases == 3 or qtd_fases == 2:
                self.f2titulo = self.f2.titulo
                self.f2drp = str(self.f2.calcular_drp()) + "%"
                self.f2drc = str(self.f2.calcular_drc()) + "%"
            else:
                self.f2titulo = ""
                self.f2drp = ""
                self.f2drc = ""
                

            if qtd_fases == 3:
                self.f3titulo = self.f3.titulo
                self.f3drp = str(self.f3.calcular_drp()) + "%"
                self.f3drc = str(self.f3.calcular_drc()) + "%"
            else:
                self.f3titulo = ""
                self.f3drp = ""
                self.f3drc = ""

            a.writelines(f"\n      Total   {self.f1.titulo}   {self.f2titulo}   {self.f3titulo}")
            a.writelines(f"\nDRP   {self.maior_drp()}%   {self.f1.calcular_drp()}%    {self.f2drp}   {self.f3drp}")
            a.writelines(f"\nDRC   {self.maior_drc()}%     {self.f1.calcular_drc()}%     {self.f2drc}     {self.f3drc}")
            a.close()

    global drp_fasea, drc_fasea, drp_faseb, drc_faseb, drp_fasec, drc_fasec, max_drp, max_drc
    global f1_maior, f1_menor, f2_maior, f2_menor, f3_maior, f3_menor

    if qtd_fases == 1:
        fase1 = fase(1)
        dados = relatorio(fase1)
        drp_fasea = fase1.calcular_drp()
        drc_fasea = fase1.calcular_drc()
        f1_maior = fase1.maiorvalorlido
        f1_menor = fase1.menorvalorlido 

    if qtd_fases == 2:
        fase1 = fase(1)
        fase2 = fase(2)
        dados = relatorio(fase1, fase2)
        drp_fasea = fase1.calcular_drp()
        drc_fasea = fase1.calcular_drc()        
        drp_faseb = fase2.calcular_drp()
        drc_faseb = fase2.calcular_drc()
        f1_maior = fase1.maiorvalorlido
        f1_menor = fase1.menorvalorlido        
        f2_menor = fase2.menorvalorlido
        f2_maior = fase2.maiorvalorlido

    if qtd_fases == 3:
        fase1 = fase(1)
        fase2 = fase(2)
        fase3 = fase(3)
        dados = relatorio(fase1, fase2, fase3)
        drp_fasea = fase1.calcular_drp()
        drc_fasea = fase1.calcular_drc()        
        drp_faseb = fase2.calcular_drp()
        drc_faseb = fase2.calcular_drc()
        drp_fasec = fase3.calcular_drp()
        drc_fasec = fase3.calcular_drc()   
        f1_maior = fase1.maiorvalorlido
        f1_menor = fase1.menorvalorlido        
        f2_menor = fase2.menorvalorlido
        f2_maior = fase2.maiorvalorlido
        f3_maior = fase3.maiorvalorlido
        f3_menor = fase3.menorvalorlido

    max_drp = dados.maior_drp()
    max_drc = dados.maior_drc()

    dados.graf_trp()
    dados.gerar_relatorio()
    dados.graf_histograma()
