# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargar_sesiones_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def __init__(self, sesiones):
        self.sesiones = sesiones
        self.comboData = []

        for s in sesiones:
            fecha = s[5]
            hora = s[4]
            seleccion = s[3]
            anio = s[2]

            item = "{} - {} - Opción {} / {}".format(fecha, hora, seleccion, anio)

            self.comboData.append(item)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 83)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 381, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setEditable(True)
        self.comboBox.addItems(self.comboData)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def enviar_respuesta(self):
        return(self.comboBox.currentIndex())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cargar sesión"))
        self.pushButton.setText(_translate("Dialog", "Aceptar"))