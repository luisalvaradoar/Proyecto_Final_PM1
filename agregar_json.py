# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar_json.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_Form(object):
    def __init__(self, anio):
        self.anio = anio

    def mensaje(self, titulo, mensaje):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def modificar_json(self):
        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '' or self.lineEdit_3.text() == '' \
        or self.lineEdit_4.text() == '' or self.lineEdit_5.text() == '' or self.lineEdit_6.text() == ''\
        or self.lineEdit_7.text() == '' or self.lineEdit_8.text() == '' or self.lineEdit_9.text() == '':
            self.mensaje("", "Llene todos los campos.")
        else:
            compra_nueva = {}

            compra_nueva["TIPO DE ENTIDAD PADRE"] = self.lineEdit.text()
            compra_nueva["TIPO DE ENTIDAD"] = self.lineEdit_2.text()
            compra_nueva["ENTIDAD COMPRADORA"] = self.lineEdit_3.text()
            compra_nueva["NOG CONCURSO"] = self.lineEdit_4.text()
            compra_nueva["MODALIDAD"] = self.lineEdit_5.text()
            compra_nueva["NIT"] = self.lineEdit_6.text()
            compra_nueva["MONTO"] = self.lineEdit_7.text()
            compra_nueva["FECHA DE PUBLICACIÓN"] = self.lineEdit_8.text()
            compra_nueva["FECHA DE ADJUDICACIÓN"] = self.lineEdit_9.text()
            compra_nueva["DESCRIPCIÓN"] = self.lineEdit_10.text()

            meses = dict(zip((1,2,3,4,5,6,7,8,9,10,11,12),('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')))
            fecha = self.lineEdit_9.text().split('-')
            mes = meses.get(int(fecha[1]))
            compra_nueva["MES DE ADJUDICACIÓN"] = mes

            if self.anio == 2016:
                with open("concursos_2016_terminado_adjudicado.json", 'r') as fp:
                    data = json.load(fp)
                
                data.append(compra_nueva)

                with open("concursos_2016_terminado_adjudicado.json", "w") as fp:
                    json.dump(data, fp, indent=0)
            elif self.anio == 2017:
                with open("concursos-publicados-2017-finalizados-adjudicados.json", 'r') as fp:
                    data = json.load(fp)
                
                data.append(compra_nueva)

                with open("concursos-publicados-2017-finalizados-adjudicados.json", "w") as fp:
                    json.dump(data, fp, indent=0)
            else:
                with open("concursos-publicados-2018-finalizados-adjudicados.json", 'r') as fp:
                    data = json.load(fp)
                
                data.append(compra_nueva)

                with open("concursos-publicados-2018-finalizados-adjudicados.json", "w") as fp:
                    json.dump(data, fp, indent=0)
            
            self.mensaje('',"Se ha agregado la nueva compra al json.")
            


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(385, 641)
        Form.setMinimumSize(QtCore.QSize(385, 641))
        Form.setMaximumSize(QtCore.QSize(385, 641))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 576))
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
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)

        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout.addWidget(self.lineEdit_9)

        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout.addWidget(self.lineEdit_10)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(430, 450, 120, 80))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 600, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.modificar_json)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Agregar datos de compra"))
        self.label.setText(_translate("Form", "Tipo de Entidad padre"))
        self.label_2.setText(_translate("Form", "Tipo de Entidad"))
        self.label_3.setText(_translate("Form", "Entidad Compradora"))
        self.label_4.setText(_translate("Form", "NOG concurso"))
        self.label_5.setText(_translate("Form", "Modalidad"))
        self.label_6.setText(_translate("Form", "NIT"))
        self.label_7.setText(_translate("Form", "Monto"))
        self.label_8.setText(_translate("Form", "Fecha de publicación"))
        self.label_9.setText(_translate("Form", "Fecha de adjudicación"))
        self.label_10.setText(_translate("Form", "Descripción"))
        self.pushButton.setText(_translate("Form", "Agregar"))