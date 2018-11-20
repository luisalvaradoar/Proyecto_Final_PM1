# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from class_email import *
from class_internet import *

class Ui_Dialog(object):
    def __init__(self, dic_u):
        self.dic_usuarios_contrasenias = dic_u

    def mensaje(self, titulo, mensaje):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def crear_usuario(self):
        usuario = self.lineEdit.text()
        contrasenia = self.lineEdit_2.text()
        conf_contrasenia = self.lineEdit_3.text()

        if usuario in self.dic_usuarios_contrasenias:
            self.mensaje("","El usuario ya esta registrado.")
            return None

        if contrasenia != conf_contrasenia:
            self.mensaje("", "Las contraseñas no coinciden.")
            return None

        if len(contrasenia) < 5:
            self.mensaje("", "La contraseña debe tener al menos 5 caracteres.")
        else:
            c1 = contrasenia.count('@')
            c2 = contrasenia.count('~')
            c3 = contrasenia.count(',')
            c4 = contrasenia.count('.')
            c5 = contrasenia.count('|')
            if c1 >= 1 or c2 >= 1 or c3 >= 1 or c4 >= 1 or c5 >= 1:
                self.usuarios_contrasenias = open('usuarios.pas', 'ba+')
                self.usuarios_contrasenias.write(b'\n')
                self.usuarios_contrasenias.write(usuario.encode('ascii'))
                self.usuarios_contrasenias.write(b' ')
                self.usuarios_contrasenias.write(contrasenia.encode('ascii'))
                self.usuarios_contrasenias.close()

                self.dic_usuarios_contrasenias.update({usuario : contrasenia})

                conexion = Internet()
                v1 = True
                if conexion.internet():
                    correo = Correo(usuario, 'Verificación')
                    correo.cuerpo("Bienvenido a los datos de la corrupcion :D")
                    try:
                        correo.enviar()
                    except Exception:
                        v1 = False
                        self.mensaje("","Usuario registrado. Aunque no se ha podido enviar el correo ya que la dirección es invalida.")

                    if v1:
                        self.mensaje("","Usuario registrado. Revisar la bandeja de entrada de {}.".format(usuario))
                else:
                    self.mensaje("","Usuario registrado. Aunque no se ha podido enviar el correo de verificacion por falta de conexion a internet.")
            else:
                self.mensaje("", "La contraseña debe contener al menos uno de los caracteres ~,.|@")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 292)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 240, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.crear_usuario)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nuevo usuario"))
        self.label.setText(_translate("Dialog", "Usuario"))
        self.label_2.setText(_translate("Dialog", "Contraseña"))
        self.label_3.setText(_translate("Dialog", "Confirmación de contraseña"))
        self.pushButton.setText(_translate("Dialog", "Crear"))

