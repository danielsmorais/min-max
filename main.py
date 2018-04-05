# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 50, 201, 381))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 100, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 130, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_1.setGeometry(QtCore.QRect(20, 70, 161, 23))
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 17))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_play = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_play.setGeometry(QtCore.QRect(60, 330, 89, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_play.setPalette(palette)
        self.pushButton_play.setAutoFillBackground(False)
        icon = QtGui.QIcon.fromTheme("play")
        self.pushButton_play.setIcon(icon)
        self.pushButton_play.setObjectName("pushButton_play")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ip.setGeometry(QtCore.QRect(60, 210, 120, 25))
        self.lineEdit_ip.setMaximumSize(QtCore.QSize(120, 25))
        self.lineEdit_ip.setWhatsThis("")
        self.lineEdit_ip.setAccessibleName("")
        self.lineEdit_ip.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_ip.setPlaceholderText("")
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 38, 25))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lineEdit_porta = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_porta.setGeometry(QtCore.QRect(60, 170, 120, 25))
        self.lineEdit_porta.setMaximumSize(QtCore.QSize(120, 25))
        self.lineEdit_porta.setWhatsThis("")
        self.lineEdit_porta.setAccessibleName("")
        self.lineEdit_porta.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhPreferNumbers)
        self.lineEdit_porta.setInputMask("")
        self.lineEdit_porta.setText("")
        self.lineEdit_porta.setPlaceholderText("")
        self.lineEdit_porta.setObjectName("lineEdit_porta")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 170, 38, 25))
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_inicia = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_inicia.setGeometry(QtCore.QRect(20, 290, 161, 25))
        self.comboBox_inicia.setObjectName("comboBox_inicia")
        self.comboBox_inicia.addItem("")
        self.comboBox_inicia.addItem("")
        self.comboBox_inicia.addItem("")
        self.comboBox_nivel = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_nivel.setGeometry(QtCore.QRect(20, 250, 161, 25))
        self.comboBox_nivel.setObjectName("comboBox_nivel")
        self.comboBox_nivel.addItem("")
        self.comboBox_nivel.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(240, 50, 371, 381))
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 331, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_1.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_9.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(120, 10, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_autor = QtWidgets.QLabel(self.centralwidget)
        self.label_autor.setGeometry(QtCore.QRect(530, 430, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_autor.setFont(font)
        self.label_autor.setObjectName("label_autor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ''' VARIAVEIS '''
        self.jog = 0
        self.click = [False, False, False, False, False, False, False, False, False]

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jogo da Velha - MIN-MAX"))
        self.radioButton_2.setText(_translate("MainWindow", "PC x Humano"))
        self.radioButton_3.setText(_translate("MainWindow", "PC x iPC"))
        self.radioButton_1.setText(_translate("MainWindow", "Humano X Humano"))
        self.label.setText(_translate("MainWindow", "CONFIGURAÇÃO"))
        self.pushButton_play.setText(_translate("MainWindow", "Jogar"))
        self.lineEdit_ip.setInputMask(_translate("MainWindow", "000.000.000.000"))
        self.lineEdit_ip.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "IP"))
        self.label_6.setText(_translate("MainWindow", "Porta"))
        self.comboBox_inicia.setItemText(0, _translate("MainWindow", "Quem inicia?"))
        self.comboBox_inicia.setItemText(1, _translate("MainWindow", "Jogador 1"))
        self.comboBox_inicia.setItemText(2, _translate("MainWindow", "Jogador 2"))
        self.comboBox_nivel.setItemText(0, _translate("MainWindow", "Fácil"))
        self.comboBox_nivel.setItemText(1, _translate("MainWindow", "Difícil"))
        self.label_title.setText(_translate("MainWindow", "Jogo da Velha / MIN-MAX"))
        self.label_autor.setText(_translate("MainWindow", "Daniel Morais"))

        self.pushButton_1.clicked.connect(self.click_1)
        self.pushButton_2.clicked.connect(self.click_2)
        self.pushButton_3.clicked.connect(self.click_3)
        self.pushButton_4.clicked.connect(self.click_4)
        self.pushButton_5.clicked.connect(self.click_5)
        self.pushButton_6.clicked.connect(self.click_6)
        self.pushButton_7.clicked.connect(self.click_7)
        self.pushButton_8.clicked.connect(self.click_8)
        self.pushButton_9.clicked.connect(self.click_9)
        self.pushButton_play.clicked.connect(self.click_play)

        self.radioButton_1.clicked.connect(self.click_r1)
        self.radioButton_2.clicked.connect(self.click_r2)
        self.radioButton_3.clicked.connect(self.click_r3)

        self.comboBox_nivel.setEnabled(False)
        self.comboBox_inicia.setEnabled(False)
        self.lineEdit_porta.setEnabled(False)
        self.lineEdit_ip.setEnabled(False)

    def click_1(self):
        if(self.click[0] == False):
            self.pushButton_1.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[0] = True

    def click_2(self):
        if(self.click[1] == False):
            self.pushButton_2.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[1] = True

    def click_3(self):
        if(self.click[2] == False):
            self.pushButton_3.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[2] = True

    def click_4(self):
        if(self.click[3] == False):
            self.pushButton_4.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[3] = True

    def click_5(self):
        if(self.click[4] == False):
            self.pushButton_5.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[4] = True

    def click_6(self):
        if(self.click[5] == False):
            self.pushButton_6.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[5] = True

    def click_7(self):
        if(self.click[6] == False):
            self.pushButton_7.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[6] = True

    def click_8(self):
        if(self.click[7] == False):
            self.pushButton_8.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[7] = True

    def click_9(self):
        if(self.click[8] == False):
            self.pushButton_9.setText(self.jog % 2 == 0 and "X" or "O")
            self.jogada()
            self.click[8] = True

    def click_play(self):
        self.pushButton_1.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")

        self.jog = 0
        self.click = [False, False, False, False, False, False, False, False, False]


    def click_r1(self):
        self.comboBox_nivel.setEnabled(False)
        self.comboBox_inicia.setEnabled(False)
        self.lineEdit_porta.setEnabled(False)
        self.lineEdit_ip.setEnabled(False)

    def click_r2(self):
        self.comboBox_nivel.setEnabled(True)
        self.comboBox_inicia.setEnabled(True)
        self.lineEdit_porta.setEnabled(False)
        self.lineEdit_ip.setEnabled(False)

    def click_r3(self):
        self.comboBox_nivel.setEnabled(True)
        self.comboBox_inicia.setEnabled(True)
        self.lineEdit_porta.setEnabled(True)
        self.lineEdit_ip.setEnabled(True)

    def jogada(self):
        if(self.jog < 8):
            self.jog += 1
        else:
            '''
            // fim de jogo
            // jogar novamente
            // limpar jogo '''
            self.jog = 0


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

