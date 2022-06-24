## Autor: Rafael Fontenele
## Neste programa é configurado e estruturado o arquivo em PDF a ser gerado.

from reportlab.pdfbase.pdfdoc import Pages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import Font, stringWidth

msg_marca = ""
msg_arquivo = "AVALIAÇÃO DE QUALIDADE DE ENERGIA"
msg_tensao_nominal = "220,00 [V]"
msg_inicio_medicao = ""
msg_final_medicao = ""
msg_lim_adequada = "Limites Tensão Adequada:"
msg_lim_precaria = "Limites Tensão Precaria:"
msg_qtd_leituras = 1008
msg_drp_fasea = 0
msg_drp_faseb = 0
msg_drp_fasec = 0
msg_drc_fasea = 0
msg_drc_faseb = 0
msg_drc_fasec = 0
msg_max_drp = 0
msg_max_drc = 0

#ordem [momentaneo, temporario, longa duração]
msg_elevacao = ["","",""]
msg_afundamento = ["","",""]
msg_interrup = ["","",""]
msg_interrupA = ["","",""]
msg_interrupB = ["","",""]
msg_interrupC = ["","",""]
msg_trm_menor = 0
msg_trm_maior = 0
#maiores e menores valores lidos em cada fase
f1_maior = 0
f2_maior = 0
f3_maior = 0
f1_menor = 0
f2_menor = 0
f3_menor = 0

def criarPDF(titulo = "", endereco_salvar = "", qtd_fases = ""):


    if titulo == "":
        titulo = "Relatório"
    
    if endereco_salvar == "":
        cnv = canvas.Canvas(titulo + ".pdf", A4)
    else:
        cnv = canvas.Canvas(endereco_salvar + "/" + titulo + ".pdf", A4)


    #bloco limites de tensão
    cnv.setFont('Helvetica-Bold', 10)
    cnv.drawString(410, 750, msg_lim_adequada)
    cnv.drawString(410, 705, msg_lim_precaria)
    cnv.setFont('Helvetica', 10)
    cnv.drawString(410, 735, "Inferior: 201,00 [V]")
    cnv.drawString(410, 720, "Superior: 231,00 [V]")
    cnv.drawString(410, 690, "Inferior: 189,00 [V]")
    cnv.drawString(410, 675, "Superior: 233,00 [V]")

    #bloco titulos
    cnv.setFont('Helvetica-Bold', 20)
    cnv.drawCentredString(297, 800, msg_arquivo)
    cnv.setFont('Helvetica-Bold', 19)
    cnv.drawCentredString(297, 777, titulo)
    cnv.setFont('Helvetica-Bold', 10)

    #bloco infos inicias topo esquerdo
    cnv.setFont('Helvetica', 10)
    cnv.drawString(20, 750, "Dispositivo: " + msg_marca)
    cnv.drawString(20, 735, "Tensão nominal: " + msg_tensao_nominal)
    cnv.drawCentredString(297.5, 750, "Início da medição: " + msg_inicio_medicao)
    cnv.drawCentredString(297.5, 735, "Término da medição: " + msg_final_medicao)
    cnv.drawString(20, 720, "Quantidade de Leituras: " + str(msg_qtd_leituras))

    #bloco dos indicadores de conformidade de tensão
    cnv.setFont('Helvetica-Bold', 10)
    cnv.drawString(20, 680, "DRP")
    cnv.drawString(20, 665, "DRC")
    cnv.drawString(60, 695, "Total")
    cnv.drawString(100, 695, "Fase A")
    
    
    cnv.setFont('Helvetica', 10)
    cnv.drawString(60, 665, str(msg_max_drc) + "%")
    cnv.drawString(60, 680, str(msg_max_drp) + "%")
    cnv.drawString(100, 680, str(msg_drp_fasea) + "%")
    cnv.drawString(100, 665, str(msg_drc_fasea) + "%")
    if qtd_fases == "2" or qtd_fases == "3":
        cnv.drawString(145, 680, str(msg_drp_faseb) + "%")
        cnv.drawString(145, 665, str(msg_drc_faseb) + "%")
        cnv.setFont('Helvetica-Bold', 10)
        cnv.drawString(145, 695, "Fase B")
    if qtd_fases == "3":    
        cnv.setFont('Helvetica', 10)
        cnv.drawString(190, 680, str(msg_drp_fasec) + "%")
        cnv.drawString(190, 665, str(msg_drc_fasec) + "%")
        cnv.setFont('Helvetica-Bold', 10)
        cnv.drawString(190, 695, "Fase C")
    
    
    #VTCDs e VTLDs maiores e menores valores
    cnv.setFont('Helvetica-Bold', 10)
    cnv.drawString(20, 620, "Elevação")
    cnv.drawString(20, 605, "Afundamento")
    cnv.drawString(20, 590, "Interrupção")
    cnv.drawString(410, 635, "Tensão em Regime Permanente")
    cnv.drawString(410, 620, "Menor valor lido: ")
    cnv.drawString(410, 560, "Maior valor lido: ")
    cnv.setFont('Helvetica', 10)
    cnv.drawString(410, 605, "Fase A: " + str(f1_menor) + " [V]")
    cnv.drawString(410, 545, "Fase A: " + str(f1_maior) + " [V]")

    if qtd_fases == "2" or qtd_fases == "3":
        cnv.setFont('Helvetica-Bold', 10)
        cnv.drawString(20, 575, "Interrupção Fase A")
        cnv.drawString(20, 560, "Interrupção Fase B")
        cnv.setFont('Helvetica', 10)
        cnv.drawString(410, 590, "Fase B: " + str(f2_menor) + " [V]")
        cnv.drawString(410, 530, "Fase B: " + str(f2_maior) + " [V]")

    if qtd_fases == "3":
        cnv.setFont('Helvetica-Bold', 10)
        cnv.drawString(20, 545, "Interrupção Fase C")
        cnv.setFont('Helvetica', 10)
        cnv.drawString(410, 575, "Fase C: " + str(f3_menor) + " [V]")
        cnv.drawString(410, 515, "Fase C: " + str(f3_maior) + " [V]")

    cnv.setFont('Helvetica-Bold', 10)
    cnv.drawCentredString(170, 635, "Momentâneo")
    cnv.drawCentredString(240, 635, "Temporário")
    cnv.drawCentredString(315, 635, "Longa Duração")
    cnv.setFont('Helvetica', 10)
    cnv.drawCentredString(170, 620, str(msg_elevacao[0]))
    cnv.drawCentredString(240, 620, str(msg_elevacao[1]))
    cnv.drawCentredString(315, 620, str(msg_elevacao[2]))
    cnv.drawCentredString(170, 605, str(msg_afundamento[0]))
    cnv.drawCentredString(240, 605, str(msg_afundamento[1]))
    cnv.drawCentredString(315, 605, str(msg_afundamento[2]))
    cnv.drawCentredString(170, 590, str(msg_interrup[0]))
    cnv.drawCentredString(240, 590, str(msg_interrup[1]))
    cnv.drawCentredString(315, 590, str(msg_interrup[2]))
    if qtd_fases == "2" or qtd_fases == "3":
        cnv.drawCentredString(170, 575, str(msg_interrupA[0]))
        cnv.drawCentredString(240, 575, str(msg_interrupA[1]))
        cnv.drawCentredString(315, 575, str(msg_interrupA[2]))
        cnv.drawCentredString(170, 560, str(msg_interrupB[0]))
        cnv.drawCentredString(240, 560, str(msg_interrupB[1]))
        cnv.drawCentredString(315, 560, str(msg_interrupB[2]))
    if qtd_fases == "3":
        cnv.drawCentredString(170, 545, str(msg_interrupC[0]))
        cnv.drawCentredString(240, 545, str(msg_interrupC[1]))
        cnv.drawCentredString(315, 545, str(msg_interrupC[2]))

     #Grafico

    if endereco_salvar == "":
        cnv.drawImage("graficotensao.png", -5, 30)
        cnv.showPage()
    else:
        cnv.drawImage(endereco_salvar + "/" + "graficotensao.png", -5, 30)
        cnv.showPage()

    if endereco_salvar == "":
        cnv.drawImage("histograma.png", -45, 60)
        cnv.showPage()
    else:
        cnv.drawImage(endereco_salvar + "/" + "histograma.png", -45, 30)
        cnv.showPage()


    cnv.save()
    #595 e 842
