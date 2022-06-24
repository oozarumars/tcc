from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(648, 540)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QtWidgets.QFrame(self.top_bar)
        self.frame_menu.setMaximumSize(QtCore.QSize(70, 40))
        self.frame_menu.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet("QPushButton{\n"
"    color: rgb(45, 45, 45);\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: 0px solid;\n"
"}\n"
"")
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_top = QtWidgets.QFrame(self.top_bar)
        self.frame_top.setMinimumSize(QtCore.QSize(550, 40))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_aviso = QtWidgets.QFrame(self.frame_top)
        self.frame_aviso.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_aviso.setMaximumSize(QtCore.QSize(500, 17))
        self.frame_aviso.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"border-radius: 5px;")
        self.frame_aviso.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_aviso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_aviso.setObjectName("frame_aviso")
        self.label_aviso = QtWidgets.QLabel(self.frame_aviso)
        self.label_aviso.setGeometry(QtCore.QRect(10, 0, 461, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_aviso.setFont(font)
        self.label_aviso.setStyleSheet("background-color: transparent;")
        self.label_aviso.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aviso.setObjectName("label_aviso")
        self.btn_aviso = QtWidgets.QPushButton(self.frame_aviso)
        self.btn_aviso.setGeometry(QtCore.QRect(480, 0, 13, 16))
        self.btn_aviso.setMaximumSize(QtCore.QSize(13, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_aviso.setFont(font)
        self.btn_aviso.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.btn_aviso.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(134, 134, 134);\n"
"}\n"
"QPushButton:pressed {\n"
"    border-radius: 5px;\n"
"    \n"
"    background-color: rgb(100,100,100);\n"
"}")
        self.btn_aviso.setObjectName("btn_aviso")
        self.progressBar = QtWidgets.QProgressBar(self.frame_aviso)
        self.progressBar.setGeometry(QtCore.QRect(7, 0, 491, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet("color: rgb(255,255,255);")
        self.btn_aviso.raise_()
        self.progressBar.raise_()
        self.progressBar.hide()
        self.label_aviso.raise_()
        self.horizontalLayout_3.addWidget(self.frame_aviso)
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.top_bar)
        self.frame_central = QtWidgets.QFrame(self.centralwidget)
        self.frame_central.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.frame_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_central.setObjectName("frame_central")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_central)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_central)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 500))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_prodist = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_prodist.setMinimumSize(QtCore.QSize(0, 70))
        self.btn_prodist.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_prodist.setFont(font)
        self.btn_prodist.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(65, 150, 255);\n"
"}")
        self.btn_prodist.setObjectName("btn_prodist")
        self.verticalLayout_4.addWidget(self.btn_prodist)
        self.btn_ajuda = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_ajuda.setMinimumSize(QtCore.QSize(0, 70))
        self.btn_ajuda.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_ajuda.setFont(font)
        self.btn_ajuda.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(65, 150, 255);\n"
"}")
        self.btn_ajuda.setObjectName("btn_ajuda")
        self.verticalLayout_4.addWidget(self.btn_ajuda)
        self.btn_info = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_info.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_info.setFont(font)
        self.btn_info.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(65, 150, 255);\n"
"}")
        self.btn_info.setObjectName("btn_info")
        self.verticalLayout_4.addWidget(self.btn_info)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.frame_central)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Paginas = QtWidgets.QStackedWidget(self.frame_pages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Paginas.sizePolicy().hasHeightForWidth())
        self.Paginas.setSizePolicy(sizePolicy)
        self.Paginas.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.Paginas.setObjectName("Paginas")
        self.page1_prodist = QtWidgets.QWidget()
        self.page1_prodist.setObjectName("page1_prodist")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page1_prodist)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame = QtWidgets.QFrame(self.page1_prodist)
        self.frame.setMinimumSize(QtCore.QSize(0, 400))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_arquivo = QtWidgets.QFrame(self.frame)
        self.frame_arquivo.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_arquivo.setStyleSheet("border-top: 1px solid  rgb(97, 97, 97);\n"
"border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_arquivo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_arquivo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_arquivo.setObjectName("frame_arquivo")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_arquivo)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.edit_arquivo = QtWidgets.QLineEdit(self.frame_arquivo)
        self.edit_arquivo.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.edit_arquivo.setFont(font)
        self.edit_arquivo.setStyleSheet("QLineEdit{\n"
"\n"
"    border: 2px solid rgb(45,45,45);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(234, 234, 0);\n"
"}")
        self.edit_arquivo.setObjectName("edit_arquivo")
        self.horizontalLayout_6.addWidget(self.edit_arquivo)
        self.button_localarquivo = QtWidgets.QPushButton(self.frame_arquivo)
        self.button_localarquivo.setMinimumSize(QtCore.QSize(65, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.button_localarquivo.setFont(font)
        self.button_localarquivo.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    color: rgb(214, 214, 214);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}")
        self.button_localarquivo.setObjectName("button_localarquivo")
        self.horizontalLayout_6.addWidget(self.button_localarquivo)
        self.verticalLayout_6.addWidget(self.frame_arquivo)
        self.frame_salvar = QtWidgets.QFrame(self.frame)
        self.frame_salvar.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_salvar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_salvar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salvar.setObjectName("frame_salvar")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_salvar)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edit_salvar = QtWidgets.QLineEdit(self.frame_salvar)
        self.edit_salvar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.edit_salvar.setFont(font)
        self.edit_salvar.setStyleSheet("QLineEdit{\n"
"\n"
"    border: 2px solid rgb(45,45,45);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(234, 234, 0);\n"
"}")
        self.edit_salvar.setObjectName("edit_salvar")
        self.horizontalLayout_7.addWidget(self.edit_salvar)
        self.button_salvar = QtWidgets.QPushButton(self.frame_salvar)
        self.button_salvar.setMinimumSize(QtCore.QSize(65, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.button_salvar.setFont(font)
        self.button_salvar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    color: rgb(214, 214, 214);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}")
        self.button_salvar.setObjectName("button_salvar")
        self.horizontalLayout_7.addWidget(self.button_salvar)
        self.verticalLayout_6.addWidget(self.frame_salvar)
        self.frame_titulo = QtWidgets.QFrame(self.frame)
        self.frame_titulo.setStyleSheet("")
        self.frame_titulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_titulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_titulo.setObjectName("frame_titulo")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_titulo)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.frame_2 = QtWidgets.QFrame(self.frame_titulo)
        self.frame_2.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(54, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border-bottom: 0px solid;")
        self.label.setObjectName("label")
        self.horizontalLayout_13.addWidget(self.label)
        self.edit_titulo = QtWidgets.QLineEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.edit_titulo.setFont(font)
        self.edit_titulo.setStyleSheet("QLineEdit{\n"
"\n"
"    border: 2px solid rgb(45,45,45);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(234, 234, 0);\n"
"}")
        self.edit_titulo.setObjectName("edit_titulo")
        self.horizontalLayout_13.addWidget(self.edit_titulo)
        self.verticalLayout_7.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setStyleSheet("border-bottom: 0px solid;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_14.addWidget(self.label_4)
        self.edit_dispositivo = QtWidgets.QLineEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.edit_dispositivo.setFont(font)
        self.edit_dispositivo.setStyleSheet("QLineEdit{\n"
"\n"
"    border: 2px solid rgb(45,45,45);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(234, 234, 0);\n"
"}")
        self.edit_dispositivo.setObjectName("edit_dispositivo")
        self.horizontalLayout_14.addWidget(self.edit_dispositivo)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.horizontalLayout_12.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_titulo)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12.addWidget(self.frame_3)
        self.verticalLayout_6.addWidget(self.frame_titulo)
        self.frame_formato = QtWidgets.QFrame(self.frame)
        self.frame_formato.setStyleSheet("")
        self.frame_formato.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_formato.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_formato.setObjectName("frame_formato")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_formato)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_6 = QtWidgets.QFrame(self.frame_formato)
        self.frame_6.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setMinimumSize(QtCore.QSize(54, 0))
        self.label_5.setStyleSheet("border-bottom: 0px solid;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_16.addWidget(self.label_5)
        self.data_inicio = QtWidgets.QDateTimeEdit(self.frame_6)
        self.data_inicio.setMaximumSize(QtCore.QSize(110, 16777215))
        self.data_inicio.setStyleSheet("")
        self.data_inicio.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.data_inicio.setObjectName("data_inicio")
        self.horizontalLayout_16.addWidget(self.data_inicio)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_formato)
        self.frame_7.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setMinimumSize(QtCore.QSize(54, 0))
        self.label_8.setStyleSheet("border-bottom: 0px solid ;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_17.addWidget(self.label_8)
        self.data_fim = QtWidgets.QDateTimeEdit(self.frame_7)
        self.data_fim.setMaximumSize(QtCore.QSize(110, 16777215))
        self.data_fim.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.data_fim.setObjectName("data_fim")
        self.horizontalLayout_17.addWidget(self.data_fim)
        self.verticalLayout_11.addWidget(self.frame_7)
        self.verticalLayout_6.addWidget(self.frame_formato)
        self.frame_fases = QtWidgets.QFrame(self.frame)
        self.frame_fases.setStyleSheet("")
        self.frame_fases.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fases.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fases.setObjectName("frame_fases")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_fases)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_10 = QtWidgets.QFrame(self.frame_fases)
        self.frame_10.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_14 = QtWidgets.QFrame(self.frame_10)
        self.frame_14.setStyleSheet("border-bottom: 0x solid;")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.check_momentos = QtWidgets.QCheckBox(self.frame_14)
        self.check_momentos.setChecked(False)
        self.check_momentos.setObjectName("check_momentos")
        self.horizontalLayout_19.addWidget(self.check_momentos)
        self.horizontalLayout_15.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_10)
        self.frame_15.setStyleSheet("border-bottom: 0x solid;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.check_salvar = QtWidgets.QCheckBox(self.frame_15)
        self.check_salvar.setObjectName("check_salvar")
        self.horizontalLayout_18.addWidget(self.check_salvar)
        self.horizontalLayout_15.addWidget(self.frame_15)
        self.verticalLayout_10.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_fases)
        self.frame_11.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setSpacing(60)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-bottom: 0x solid;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.radio_csv = QtWidgets.QRadioButton(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.radio_csv.setFont(font)
        self.radio_csv.setStyleSheet("border-bottom: 0x solid;\n"
"color: rgb(0, 0, 0);")
        self.radio_csv.setChecked(True)
        self.radio_csv.setObjectName("radio_csv")
        self.horizontalLayout_8.addWidget(self.radio_csv)
        self.radio_xlsx = QtWidgets.QRadioButton(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.radio_xlsx.setFont(font)
        self.radio_xlsx.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-bottom: 0x solid;")
        self.radio_xlsx.setObjectName("radio_xlsx")
        self.horizontalLayout_8.addWidget(self.radio_xlsx)
        self.verticalLayout_10.addWidget(self.frame_11)
        self.verticalLayout_6.addWidget(self.frame_fases)
        self.frame_leituras = QtWidgets.QFrame(self.frame)
        self.frame_leituras.setStyleSheet("")
        self.frame_leituras.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_leituras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_leituras.setObjectName("frame_leituras")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_leituras)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_9 = QtWidgets.QFrame(self.frame_leituras)
        self.frame_9.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-bottom: 0x solid;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_9.addWidget(self.label_2)
        self.spin_fases = QtWidgets.QSpinBox(self.frame_9)
        self.spin_fases.setMinimumSize(QtCore.QSize(50, 0))
        self.spin_fases.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_fases.setStyleSheet("color: rgb(0, 0, 0);")
        self.spin_fases.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_fases.setMinimum(1)
        self.spin_fases.setMaximum(3)
        self.spin_fases.setProperty("value", 3)
        self.spin_fases.setObjectName("spin_fases")
        self.horizontalLayout_9.addWidget(self.spin_fases)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_leituras)
        self.frame_8.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-bottom: 0x solid;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.spin_leituras = QtWidgets.QSpinBox(self.frame_8)
        self.spin_leituras.setMinimumSize(QtCore.QSize(50, 0))
        self.spin_leituras.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.spin_leituras.setFont(font)
        self.spin_leituras.setStyleSheet("color: rgb(0, 0, 0);")
        self.spin_leituras.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_leituras.setMinimum(1)
        self.spin_leituras.setMaximum(1008)
        self.spin_leituras.setSingleStep(5)
        self.spin_leituras.setProperty("value", 1008)
        self.spin_leituras.setObjectName("spin_leituras")
        self.horizontalLayout_10.addWidget(self.spin_leituras)
        self.verticalLayout_9.addWidget(self.frame_8)
        self.verticalLayout_6.addWidget(self.frame_leituras)
        self.frame_botoes = QtWidgets.QFrame(self.frame)
        self.frame_botoes.setStyleSheet("border-bottom: 1px solid  rgb(97, 97, 97);")
        self.frame_botoes.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_botoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes.setObjectName("frame_botoes")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_botoes)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_gerar = QtWidgets.QPushButton(self.frame_botoes)
        self.btn_gerar.setMinimumSize(QtCore.QSize(90, 20))
        self.btn_gerar.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btn_gerar.setFont(font)
        self.btn_gerar.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(30, 30, 30);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}")
        self.btn_gerar.setObjectName("btn_gerar")
        self.horizontalLayout_11.addWidget(self.btn_gerar)
        self.btn_sair = QtWidgets.QPushButton(self.frame_botoes)
        self.btn_sair.setMinimumSize(QtCore.QSize(90, 20))
        self.btn_sair.setMaximumSize(QtCore.QSize(90, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btn_sair.setFont(font)
        self.btn_sair.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 30, 30);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}")
        self.btn_sair.setObjectName("btn_sair")
        self.horizontalLayout_11.addWidget(self.btn_sair)
        self.verticalLayout_6.addWidget(self.frame_botoes)
        self.horizontalLayout_5.addWidget(self.frame)
        self.Paginas.addWidget(self.page1_prodist)
        self.page2_ajuda = QtWidgets.QWidget()
        self.page2_ajuda.setObjectName("page2_ajuda")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page2_ajuda)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_notas = QtWidgets.QFrame(self.page2_ajuda)
        self.frame_notas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_notas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_notas.setObjectName("frame_notas")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_notas)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_13 = QtWidgets.QFrame(self.frame_notas)
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_13.setStyleSheet("")
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.verticalLayout_14.addWidget(self.frame_13)
        self.frame_imagem_exemplo = QtWidgets.QFrame(self.frame_notas)
        self.frame_imagem_exemplo.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_imagem_exemplo.setStyleSheet("\n"
"image: url(:/icones/exemploplanilha.PNG);")
        self.frame_imagem_exemplo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_imagem_exemplo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_imagem_exemplo.setObjectName("frame_imagem_exemplo")
        self.verticalLayout_14.addWidget(self.frame_imagem_exemplo)
        self.verticalLayout_12.addWidget(self.frame_notas, 0, QtCore.Qt.AlignHCenter)
        self.Paginas.addWidget(self.page2_ajuda)
        self.page3_info = QtWidgets.QWidget()
        self.page3_info.setObjectName("page3_info")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.page3_info)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_12 = QtWidgets.QFrame(self.page3_info)
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.frame_12)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.verticalLayout_15.addWidget(self.frame_12)
        self.Paginas.addWidget(self.page3_info)
        self.verticalLayout_5.addWidget(self.Paginas)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.frame_central)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Paginas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HAL 9000 v1.0"))
        self.btn_menu.setText(_translate("MainWindow", "Menu"))
        self.label_aviso.setText(_translate("MainWindow", "Bem-vindo ao HAL 9000 v1.0"))
        self.btn_aviso.setText(_translate("MainWindow", "X"))
        self.btn_prodist.setText(_translate("MainWindow", "PRODIST"))
        self.btn_ajuda.setText(_translate("MainWindow", "Ajuda"))
        self.btn_info.setText(_translate("MainWindow", "Informações"))
        self.edit_arquivo.setPlaceholderText(_translate("MainWindow", "Escolha um arquivo"))
        self.button_localarquivo.setText(_translate("MainWindow", "Procurar"))
        self.edit_salvar.setPlaceholderText(_translate("MainWindow", "Escolha o destino para salvar (auto: local do programa)"))
        self.button_salvar.setText(_translate("MainWindow", "Procurar"))
        self.label.setText(_translate("MainWindow", "Titulo:"))
        self.edit_titulo.setPlaceholderText(_translate("MainWindow", "Identificador da medição"))
        self.label_4.setText(_translate("MainWindow", "Dispositivo:"))
        self.edit_dispositivo.setPlaceholderText(_translate("MainWindow", "Modelo/Marca (ex: Kron/Mult K NG)"))
        self.label_5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Início da medição:</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Fim da medição:</p></body></html>"))
        self.check_momentos.setText(_translate("MainWindow", "Considerar momentos da medição escolhidos"))
        self.check_salvar.setText(_translate("MainWindow", "Salvar imagens (gráficos e histogramas)"))
        self.label_6.setText(_translate("MainWindow", "Formato do arquivo:"))
        self.radio_csv.setText(_translate("MainWindow", ".csv ou .txt (delimitado por ;)"))
        self.radio_xlsx.setText(_translate("MainWindow", ".xlsx"))
        self.label_2.setText(_translate("MainWindow", "Quantidade de fases:"))
        self.label_3.setText(_translate("MainWindow", "Quantidade de leituras:"))
        self.btn_gerar.setText(_translate("MainWindow", "Gerar relatório"))
        self.btn_sair.setText(_translate("MainWindow", "Sair"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-weight:600;\">Nota 1:</span> Instalar as bibliotecas PyQt5, matplotlib, pandas, OpenPyXL e reportlab.</p><p align=\"justify\">(usar comando pip install &quot;nome da biblioteca&quot; no prompt de comando, caso esteja usando o arquivo </p><p align=\"justify\">em .py)</p><p align=\"justify\"><span style=\" font-weight:600;\">Nota 2:</span> O arquivo deve seguir o padrão da planilha mostrado na figura abaixo, exceto a </p><p align=\"justify\">parte do horário que é o opcional. (atentar a questão de espaços desnecessários e acentos)</p><p align=\"justify\"><span style=\" font-weight:600;\">Nota 3:</span> O programa está baseado no PRODIST Módulo 8 Revisão 12 (2021)</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Universidade Federal do Tocantins - Câmpus Palmas</span></p><p align=\"center\">Programa Desenvolvido para o Projeto de Gradução</p><p align=\"center\">Título do projeto: Metodologia para Obtenção dos Indicadores de Conformidade de Tensão</p><p align=\"center\">Aluno: Rafael Fontenele Moraes Cutrim</p><p align=\"center\">Orientador: Prof. Msc. Alex Vilarindo Menezes</p><p align=\"center\">Contato: rafaelfontenele4@gmail.com</p><p align=\"center\"><br/></p><p align=\"center\">2021</p></body></html>"))
import resources


"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
