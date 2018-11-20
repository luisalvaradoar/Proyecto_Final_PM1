# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio_de_secion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from pantalla_principal import Ui_MainWindow
from class_email import *
from class_internet import *

class Ui_Form(object):
    def __init__(self):
        self.usuarios_contrasenias = open('usuarios.pas', 'rb')
        self.usuarios = []
        self.contrasenias = []
        while(True):
            linea = self.usuarios_contrasenias.readline().decode('utf-8')
            if linea == '':
                break
            else:
                uc = linea.replace('\n', '').split(' ')
                self.usuarios.append(uc[0])
                self.contrasenias.append(uc[1])
        self.dic_usuarios_contrasenias = dict(zip(self.usuarios, self.contrasenias))
        self.usuarios_contrasenias.close()

    def mensaje(self, titulo, mensaje):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def iniciar_secion(self):
        usuario = self.lineEdit.text()
        contrasenia = self.lineEdit_2.text()
        
        if usuario in self.dic_usuarios_contrasenias:
            if self.dic_usuarios_contrasenias.get(usuario) == contrasenia:
                self.pantallaPrincipal = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow(usuario)
                self.ui.setupUi(self.pantallaPrincipal)
                self.pantallaPrincipal.show()
            else:
                self.mensaje("asd","La contraseña es incorrecta.")
        else:
            self.mensaje("", "El usuario '{}' no esta registrado.".format(usuario))
    
    def crear_usuario(self):
        usuario = self.lineEdit.text()
        contrasenia = self.lineEdit_2.text()
        if usuario in self.dic_usuarios_contrasenias:
            self.mensaje("","El usuario ya esta registrado.")
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

    def recuperar_contra(self):
        usuario = self.lineEdit.text()
        conexion = Internet()
        if usuario in self.dic_usuarios_contrasenias:
            contra = self.dic_usuarios_contrasenias.get(usuario)
            if conexion.internet():
                correo = Correo(usuario, 'Recuperación de contraseña')
                correo.cuerpo('La contraseña del usuario {} es "{}".'.format(usuario, contra))
                correo.enviar()
                self.mensaje("", "Se ha enviado un correo a {} con la contraseña".format(self.lineEdit.text()))
            else:
                self.mensaje("", "No hay conexion a internet.")
        else:
            self.mensaje("", "El usuario '{}' no esta registrado.".format(usuario))

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(489, 335)
        Form.setMinimumSize(QtCore.QSize(489, 335))
        Form.setMaximumSize(QtCore.QSize(489, 335))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 30, 201, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 60, 16))
        self.label_3.setObjectName("label_3")
        self.imagen = QtWidgets.QLabel(Form)
        self.imagen.setPixmap(QtGui.QPixmap('logo.png'))
        self.imagen.setGeometry(50, 10, 85, 95)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 150, 175, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 200, 175, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ver_contrasenia = QtWidgets.QRadioButton(Form)
        self.ver_contrasenia.setGeometry(QtCore.QRect(40, 230, 161, 20))
        self.ver_contrasenia.setObjectName("ver_contrasenia")
        self.ver_contrasenia.clicked.connect(self.ver_contra)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 180, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.crear_usuario)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 150, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.iniciar_secion)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 210, 191, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.recuperar_contra)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 451, 16))
        self.label_6.setObjectName("label_6")

        # self.botonAbrirSesion = QtWidgets.QPushButton(Form)
        # self.botonAbrirSesion.setGeometry(QtCore.QRect(250, 170, 113, 32))
        # self.botonAbrirSesion.setObjectName("botonAbrirSesion")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ver_contra(self):
        if self.ver_contrasenia.isChecked():
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Inicio de sesión"))
        self.label.setText(_translate("Form", "Luis Alfredo Alvarado Rodríguez"))
        self.label_2.setText(_translate("Form", "201612241"))
        self.label_3.setText(_translate("Form", "Usuario"))
        #self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_5.setText(_translate("Form", "Contraseña"))
        self.ver_contrasenia.setText(_translate("Form", "Ver contraseña"))
        self.pushButton.setText(_translate("Form", "Crear usuario"))
        self.pushButton_2.setText(_translate("Form", "Ingresar"))
        self.pushButton_3.setText(_translate("Form", "Recuperar mi contraseña"))
        self.label_6.setText(_translate("Form", "Para iniciar una sesión de invitado, use como usuario y contraseña ECFM"))
        # self.botonAbrirSesion.setText(_translate("Form", "Abir sesión"))