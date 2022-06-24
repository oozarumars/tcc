from PyQt5.QtWidgets import QMainWindow
from interface import *
from tkinter import filedialog
import relatorio
import gerar_pdf
import sys
import os

class MainWindow(QMainWindow):
    def abrir_arquivo(self):
        arquivo = filedialog.askopenfilename()
        self.ui.edit_arquivo.setText(arquivo)

    def salvar_arquivo(self):
        arquivo = filedialog.askdirectory()
        self.ui.edit_salvar.setText(arquivo)
        

    def formato_arquivo(self):
        if self.ui.radio_xlsx.isChecked() == True:
            relatorio.opcao_formato = 1
        elif self.ui.radio_csv.isChecked() == True:
            relatorio.opcao_formato = 0

    def opcoes_arquivo_up(self):
        if self.ui.check_salvar.isChecked() == False:
            try:
                os.remove(self.ui.edit_salvar.text() + "/histograma.png")
                os.remove(self.ui.edit_salvar.text() + "/graficotensao.png")
            except:
                os.remove("histograma.png")
                os.remove("graficotensao.png")

    def opcoes_arquivo_back(self):    
        relatorio.qtd_fases = int(self.ui.spin_fases.text())
        relatorio.qtd_leituras = int(self.ui.spin_leituras.text())
        relatorio.endereco = self.ui.edit_arquivo.text()
        relatorio.endereco_salvar = self.ui.edit_salvar.text()

    def manipular_pdf(self):
        gerar_pdf.msg_marca = self.ui.edit_dispositivo.text()
        gerar_pdf.msg_qtd_leituras = int(self.ui.spin_leituras.text())

        #VTCDS e LDS
        for k in range (0,3):
            gerar_pdf.msg_elevacao[k] = int(relatorio.elev[k])
            gerar_pdf.msg_afundamento[k] = int(relatorio.afun[k])
            gerar_pdf.msg_interrup[k] = int(relatorio.interrup[k])
            if self.ui.spin_fases.text() == "2" or "3":
                gerar_pdf.msg_interrupA[k] = int(relatorio.interrupa[k])
                gerar_pdf.msg_interrupB[k] = int(relatorio.interrupb[k])
            if self.ui.spin_fases.text() == "3":
                gerar_pdf.msg_interrupC[k] = int(relatorio.interrupc[k])
        #
        gerar_pdf.msg_drp_fasea = relatorio.drp_fasea
        gerar_pdf.msg_drc_fasea = relatorio.drc_fasea
        gerar_pdf.msg_drp_faseb = relatorio.drp_faseb
        gerar_pdf.msg_drc_faseb = relatorio.drc_faseb
        gerar_pdf.msg_drp_fasec = relatorio.drp_fasec
        gerar_pdf.msg_drc_fasec = relatorio.drc_fasec
        gerar_pdf.msg_max_drp = relatorio.max_drp
        gerar_pdf.msg_max_drc = relatorio.max_drc
        #
        gerar_pdf.f1_maior = relatorio.f1_maior
        gerar_pdf.f2_maior = relatorio.f2_maior
        gerar_pdf.f3_maior = relatorio.f3_maior
        gerar_pdf.f1_menor = relatorio.f1_menor
        gerar_pdf.f2_menor = relatorio.f2_menor
        gerar_pdf.f3_menor = relatorio.f3_menor
        #


        if self.ui.check_momentos.isChecked() == True:
            gerar_pdf.msg_inicio_medicao = self.ui.data_inicio.text()
            gerar_pdf.msg_final_medicao = self.ui.data_fim.text()
        else:
            try:
                gerar_pdf.msg_inicio_medicao = relatorio.inicio_medicao
                gerar_pdf.msg_final_medicao = relatorio.final_medicao
            except:
                self.ui.label_aviso.setText("Data inválida")


    def executar(self):
        try:
            self.ui.frame_aviso.show()
            self.ui.frame_aviso.setStyleSheet("background-color: transparent;")
            self.ui.btn_aviso.hide()
            self.ui.label_aviso.show()
            self.ui.progressBar.show()
            #
            self.ui.label_aviso.setText("Carregando dados do arquivo")
            self.ui.progressBar.setProperty("value", 20)
            self.opcoes_arquivo_back()
            #
            self.ui.label_aviso.setText("Checando formato do arquivo")
            self.ui.progressBar.setProperty("value", 37)
            self.formato_arquivo()
            #
            self.ui.label_aviso.setText("Gerando gráficos e dados estátisticos")
            self.ui.progressBar.setProperty("value", 52)
            relatorio.executar()
            #
            self.ui.label_aviso.setText("Gerando PDF")
            self.ui.progressBar.setProperty("value", 73)
            self.manipular_pdf()
            gerar_pdf.criarPDF(self.ui.edit_titulo.text(), self.ui.edit_salvar.text(), self.ui.spin_fases.text())
            #
            self.ui.label_aviso.setText("Checando informações")
            self.ui.progressBar.setProperty("value", 97)
            self.opcoes_arquivo_up()
            #
            self.ui.label_aviso.setText("Relatório gerado")
            self.ui.progressBar.setProperty("value", 100)
            self.ui.progressBar.hide()
            self.ui.frame_aviso.setStyleSheet("background-color: rgb(85, 170, 255);\nborder-radius: 5px;")
            self.ui.btn_aviso.show()
            #
            
        except:
            self.ui.progressBar.hide()
            self.ui.frame_aviso.setStyleSheet("background-color: rgb(85, 170, 255);\nborder-radius: 5px;")
            self.ui.label_aviso.setStyleSheet("background-color: transparent;\n color: rgb(0,0,0);")
            self.ui.label_aviso.setText("Erro")
            self.ui.frame_aviso.show()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Atribuindo ação aos botões criados    

        self.ui.btn_aviso.clicked.connect(lambda: self.ui.frame_aviso.hide())

        self.ui.button_localarquivo.clicked.connect(lambda: self.abrir_arquivo())
        
        self.ui.button_salvar.clicked.connect(lambda: self.salvar_arquivo())

        self.ui.btn_prodist.clicked.connect(lambda: self.ui.Paginas.setCurrentWidget(self.ui.page1_prodist))

        self.ui.btn_ajuda.clicked.connect(lambda: self.ui.Paginas.setCurrentWidget(self.ui.page2_ajuda))

        self.ui.btn_info.clicked.connect(lambda: self.ui.Paginas.setCurrentWidget(self.ui.page3_info))

        self.ui.btn_sair.clicked.connect(lambda: app.closeAllWindows())    

        self.ui.btn_gerar.clicked.connect(lambda: self.executar())

        self.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())