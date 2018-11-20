# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pantalla_principal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import pickle
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from agregar_json import Ui_Form
from cargar_sesiones import Ui_Dialog
from class_internet import *
from class_lectura_json import *
from class_lectura_API import *
from class_reporte import *

class Ui_MainWindow(object):
    def __init__(self, usuario):
        self.usuario = usuario
        self.anio = None
        self.seleccion = None
        self.nog_concurso = None
        self.descripciones = None
        self.resultado = None

    def lectura_de_datos(self, anio):
        self.pushButton_reporte.setEnabled(True)
        conexion = Internet()
        if anio == 2016:
            self.anio = 2016
            if self.op1_2016.isChecked():
                if conexion.internet():
                    print("API")
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 1
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion1()
            elif self.op2_2016.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 2
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion2()
            elif self.op3_2016.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 3
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion3()
            elif self.op4_2016.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 4
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion4()
            else:
                self.mensaje("", "Seleccione una opción.")
        elif anio == 2017:
            self.anio = 2017
            if self.op1_2017.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 1
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion1()
            elif self.op2_2017.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 2
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion2()
            elif self.op3_2017.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 3
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion3()
            elif self.op4_2017.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 4
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion4()
            else:
                self.mensaje("", "Seleccione una opción.")
        else:
            self.anio = 2018
            if self.op1_2018.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 1
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion1()
            elif self.op2_2018.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 2
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion2()
            elif self.op3_2018.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 3
                self.descripciones = datos.getDescripciones()
                self.nog_concurso = datos.getNogConcurso()
                self.resultado = datos.opcion3()
            elif self.op4_2018.isChecked():
                if conexion.internet():
                    datos = Lectura_de_Datos_API(anio)
                else:
                    datos = Lectura_de_Datos_json(anio)
                self.seleccion = 4
                self.resultado = datos.opcion4()
            else:
                self.mensaje("", "Seleccione una opción.")

    def mensaje(self, titulo, mensaje):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def agregar_json(self, anio):
        self.agjson = QtWidgets.QMainWindow()
        self.ui = Ui_Form(anio)
        self.ui.setupUi(self.agjson)
        self.agjson.show()

    def generar_reporte(self):
        if self.seleccion == None:
            self.mensaje('',"No se ha seleccionado que datos analizar.")
            return None

        if self.seleccion == 1:
            titulo = "Compras m\\'as grandes"
        elif self.seleccion == 2:
            titulo = "Compra m\\'as grande realizadas por mes"
        elif self.seleccion == 3:
            titulo = "Compras m\\'as grandes realizadas por la USAC"
        else:
            titulo = "Top 10 de los proveedores que m\\'as vendieron"

        file = MiReporte("Graficas_y_analisis")
        file.iniciarReporte(titulo, self.usuario, str(self.anio))
        if self.seleccion != 4:
            file.setSection('Tabla')
            file.iniciarCentrar()
            file.iniciarTabla(3, ('No', 'NOG concurso', 'Monto'))

            for i in self.resultado:
                monto = str(i[0])
                nog_concurso = self.nog_concurso[i[1]]
                file.escribirFila((nog_concurso, monto))
            file.terminarTabla()
            file.terminarCentrar()
            
            file.setSection('Grafica')
            file.iniciarCentrar()
            file.iniciarGrafica(len(self.resultado))
            for i in self.resultado:
                file.agregarBarra(str(i[0]))
            file.terminarGrafica()
            file.terminarCentrar()

            file.setSection('Descripción')
            file.iniciarLista()
            for i in self.resultado:
                des = self.descripciones[i[1]]
                if '<br />' in des:
                    des = des.replace('<br />','')
                file.agregarItem(des)
            file.terminarLista()
        else:
            file.setSection('Tabla')
            file.iniciarCentrar()
            file.iniciarTabla(3, ('No', 'NIT', 'Monto'))

            for i in self.resultado:
                nit = i[0]
                monto = str(i[1])
                file.escribirFila((nit, monto))
            file.terminarTabla()
            file.terminarCentrar()

            file.setSection('Grafica')
            file.iniciarCentrar()
            file.iniciarGrafica(len(self.resultado))
            for i in self.resultado:
                file.agregarBarra(str(i[1]))
            file.terminarGrafica()
            file.terminarCentrar()
            
        file.terminarReporte()
        file.compilarReporte()
        self.mensaje('','El reporte se genero con éxito. El archivo se llama "Graficas_y_analisis.pdf"')

    def menu(self, opcion):
        if opcion.text() == 'Guardar sesión':
            if self.resultado != None:
                fecha = datetime.datetime.now().strftime ("%d/%m/%Y")
                hora = datetime.datetime.now().time().strftime("%H:%M")
                datos_a_guardar = (self.usuario, self.resultado, self.anio, self.seleccion, hora, fecha, self.nog_concurso)#, self.descripciones)
                archivo_binario = open("sesiones.ses", mode= 'ba+')
                archivo_binario.write(b'comienza \n')
                pickle.dump(datos_a_guardar, archivo_binario)
                archivo_binario.write(b'\n termina \n')
                archivo_binario.close()
                self.mensaje('','Sesión guardada')
            else:
                self.mensaje('',"Aún no se ha generado ningún reporte")
        elif opcion.text() == 'Abrir sesión':
            sesiones = []
            archivo_binario = open("sesiones.ses", "br")
            while(True):
                linea = archivo_binario.readline()
                if linea == b'comienza \n':
                    vaciado = archivo_binario.readline()
                    while(True):
                        linea_nueva = archivo_binario.readline()
                        if linea_nueva != b' termina \n':
                            vaciado += linea_nueva
                        else:
                            sesiones.append(pickle.loads(vaciado))
                            break
                else:
                    break
            
            sesiones_del_usuario = []
            for s in sesiones:
                if s[0] == self.usuario:
                    sesiones_del_usuario.append(s)

            self.abrir_sesion = QtWidgets.QDialog()
            self.ui = Ui_Dialog(sesiones_del_usuario)
            self.ui.setupUi(self.abrir_sesion)
            self.abrir_sesion.show()

            if self.abrir_sesion.exec_() == 0:
                rsp = self.ui.enviar_respuesta()
            
            sesion_iniciada = sesiones_del_usuario[rsp]

            self.resultado = sesion_iniciada[1]
            self.anio = sesion_iniciada[2]
            self.seleccion = sesion_iniciada[3]
            self.nog_concurso = sesion_iniciada[-1]
            #self.descripciones = sesion_iniciada[-1]


            self.generar_grafica()
            self.generar_tabla()
            self.pushButton_reporte.setEnabled(False)
            self.mensaje('',"Sesión cargada con exito.")
            

    def generar_grafica(self):
        if self.resultado == None:
            return(None)

        if self.seleccion in (1,3):
            mas_grande = max(self.resultado)[0]

            proporciones = []
            for r in self.resultado:
                proporciones.append(int((r[0] / mas_grande)*250))
            
            self.barra1.resize(20, proporciones[0])
            self.barra1.move(10, 275 - proporciones[0])
            self.barra2.resize(20, proporciones[1])
            self.barra2.move(40, 275 - proporciones[1])
            self.barra3.resize(20, proporciones[2])
            self.barra3.move(70, 275 - proporciones[2])
            self.barra4.resize(20, proporciones[3])
            self.barra4.move(100, 275 - proporciones[3])
            self.barra5.resize(20, proporciones[4])
            self.barra5.move(130, 275 - proporciones[4])
            self.barra6.resize(20, proporciones[5])
            self.barra6.move(160, 275 - proporciones[5])
            self.barra7.resize(20, proporciones[6])
            self.barra7.move(190, 275 - proporciones[6])
            self.barra8.resize(20, proporciones[7])
            self.barra8.move(220, 275 - proporciones[7])
            self.barra9.resize(20, proporciones[8])
            self.barra9.move(250, 275 - proporciones[8])
            self.barra10.resize(20, proporciones[9])
            self.barra10.move(280, 275 - proporciones[9])
            self.barra11.resize(20, 0)
            self.barra11.move(310, 275)
            self.barra12.resize(20, 0)
            self.barra12.move(340, 275)

            self.nombre1.setText("(1)")
            self.nombre2.setText("(2)")
            self.nombre3.setText("(3)")
            self.nombre4.setText("(4)")
            self.nombre5.setText("(5)")
            self.nombre6.setText("(6)")
            self.nombre7.setText("(7)")
            self.nombre8.setText("(8)")
            self.nombre9.setText("(9)")
            self.nombre10.setText("(10)")
            self.nombre11.setText("")
            self.nombre12.setText("")

        elif self.seleccion == 2:
            mas_grande = max(self.resultado)[0]

            proporciones = []
            for r in self.resultado:
                proporciones.append(int((r[0] / mas_grande)*250))
            
            self.barra1.resize(20, proporciones[0])
            self.barra1.move(10, 275 - proporciones[0])
            self.barra2.resize(20, proporciones[1])
            self.barra2.move(40, 275 - proporciones[1])
            self.barra3.resize(20, proporciones[2])
            self.barra3.move(70, 275 - proporciones[2])
            self.barra4.resize(20, proporciones[3])
            self.barra4.move(100, 275 - proporciones[3])
            self.barra5.resize(20, proporciones[4])
            self.barra5.move(130, 275 - proporciones[4])
            self.barra6.resize(20, proporciones[5])
            self.barra6.move(160, 275 - proporciones[5])
            self.barra7.resize(20, proporciones[6])
            self.barra7.move(190, 275 - proporciones[6])
            self.barra8.resize(20, proporciones[7])
            self.barra8.move(220, 275 - proporciones[7])
            self.barra9.resize(20, proporciones[8])
            self.barra9.move(250, 275 - proporciones[8])
            self.barra10.resize(20, proporciones[9])
            self.barra10.move(280, 275 - proporciones[9])
            self.barra11.resize(20, proporciones[10])
            self.barra11.move(310, 275 - proporciones[10])
            self.barra12.resize(20, proporciones[11])
            self.barra12.move(340, 275 - proporciones[11])

            self.nombre1.setText("(1)")
            self.nombre2.setText("(2)")
            self.nombre3.setText("(3)")
            self.nombre4.setText("(4)")
            self.nombre5.setText("(5)")
            self.nombre6.setText("(6)")
            self.nombre7.setText("(7)")
            self.nombre8.setText("(8)")
            self.nombre9.setText("(9)")
            self.nombre10.setText("(10)")
            self.nombre11.setText("(11)")
            self.nombre12.setText("(12)")
        else:
            mas_grande = self.resultado[9][1]

            proporciones = []
            for r in self.resultado:
                proporciones.append(int((r[1] / mas_grande)*250))
            
            self.barra1.resize(20, proporciones[0])
            self.barra1.move(10, 275 - proporciones[0])
            self.barra2.resize(20, proporciones[1])
            self.barra2.move(40, 275 - proporciones[1])
            self.barra3.resize(20, proporciones[2])
            self.barra3.move(70, 275 - proporciones[2])
            self.barra4.resize(20, proporciones[3])
            self.barra4.move(100, 275 - proporciones[3])
            self.barra5.resize(20, proporciones[4])
            self.barra5.move(130, 275 - proporciones[4])
            self.barra6.resize(20, proporciones[5])
            self.barra6.move(160, 275 - proporciones[5])
            self.barra7.resize(20, proporciones[6])
            self.barra7.move(190, 275 - proporciones[6])
            self.barra8.resize(20, proporciones[7])
            self.barra8.move(220, 275 - proporciones[7])
            self.barra9.resize(20, proporciones[8])
            self.barra9.move(250, 275 - proporciones[8])
            self.barra10.resize(20, proporciones[9])
            self.barra10.move(280, 275 - proporciones[9])
            self.barra11.resize(20, 0)
            self.barra11.move(310, 275)
            self.barra12.resize(20, 0)
            self.barra12.move(340, 275)

            self.nombre1.setText("(1)")
            self.nombre2.setText("(2)")
            self.nombre3.setText("(3)")
            self.nombre4.setText("(4)")
            self.nombre5.setText("(5)")
            self.nombre6.setText("(6)")
            self.nombre7.setText("(7)")
            self.nombre8.setText("(8)")
            self.nombre9.setText("(9)")
            self.nombre10.setText("(10)")
            self.nombre11.setText("")
            self.nombre12.setText("")

    
    def generar_tabla(self):
        if self.resultado == None:
            return(None)

        titulos = ("Compras más grandes","Compra más grande realizadas por mes","Compras más grandes realizadas por la USAC","Top 10 de los proveedores que más vendieron")
        encabezado = '{} del año {}'.format(titulos[self.seleccion -1], self.anio)
        self.titulo.setText(encabezado)
        
        if self.seleccion in (1,3,4):
            for i in (11, 12):
                for j in range(3):
                    item = QtWidgets.QTableWidgetItem()
                    self.tableWidget.setItem(i, j, item)
                    item = self.tableWidget.item(i,j)
                    item.setText("")
        else:
            item = self.tableWidget.item(11,0)
            item.setText("11")
            item = self.tableWidget.item(12,0)
            item.setText("12")

        if self.seleccion in (1,2,3):
            item = self.tableWidget.item(0, 1)
            item.setText("NOG")
            
            i = 1
            for r in self.resultado:
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, 1, item)
                item = self.tableWidget.item(i, 1)
                item.setText(str( self.nog_concurso[r[1]] ))

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, 2, item)
                item = self.tableWidget.item(i, 2)
                item.setText(str(r[0]))
                i += 1
        else:
            item = self.tableWidget.item(0, 1)
            item.setText("NIT")

            i = 1
            for r in self.resultado:
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, 1, item)
                item = self.tableWidget.item(i, 1)
                item.setText(str( r[0] ))

                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, 2, item)
                item = self.tableWidget.item(i, 2)
                item.setText(str(r[1]))
                i += 1

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 454)
        MainWindow.setMinimumSize(QtCore.QSize(813, 454))
        MainWindow.setMaximumSize(QtCore.QSize(813, 454))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 791, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.op1_2016 = QtWidgets.QRadioButton(self.tab)
        self.op1_2016.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.op1_2016.setObjectName("op1_2016")
        self.op2_2016 = QtWidgets.QRadioButton(self.tab)
        self.op2_2016.setGeometry(QtCore.QRect(30, 70, 271, 20))
        self.op2_2016.setObjectName("op2_2016")
        self.op3_2016 = QtWidgets.QRadioButton(self.tab)
        self.op3_2016.setGeometry(QtCore.QRect(30, 100, 301, 20))
        self.op3_2016.setObjectName("op3_2016")
        self.op4_2016 = QtWidgets.QRadioButton(self.tab)
        self.op4_2016.setGeometry(QtCore.QRect(30, 130, 301, 20))
        self.op4_2016.setObjectName("op4_2016")
        self.pushButton_2016 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2016.setGeometry(QtCore.QRect(230, 180, 113, 32))
        self.pushButton_2016.setObjectName("pushButton_2016")
        self.pushButton_2016.clicked.connect(lambda: self.lectura_de_datos(2016))
        self.pushButton_2016.clicked.connect(self.generar_grafica)
        self.pushButton_2016.clicked.connect(self.generar_tabla)
        self.pushButton_2016_json = QtWidgets.QPushButton(self.tab)
        self.pushButton_2016_json.setGeometry(QtCore.QRect(230, 210, 113, 32))
        self.pushButton_2016_json.setObjectName("pushButton_2016_json")
        self.pushButton_2016_json.clicked.connect(lambda: self.agregar_json(2016))

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setObjectName("label_2")
        self.op1_2017 = QtWidgets.QRadioButton(self.tab_2)
        self.op1_2017.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.op1_2017.setObjectName("op1_2017")
        self.op2_2017 = QtWidgets.QRadioButton(self.tab_2)
        self.op2_2017.setGeometry(QtCore.QRect(30, 70, 271, 20))
        self.op2_2017.setObjectName("op2_2017")
        self.op3_2017 = QtWidgets.QRadioButton(self.tab_2)
        self.op3_2017.setGeometry(QtCore.QRect(30, 100, 301, 20))
        self.op3_2017.setObjectName("op3_2017")
        self.op4_2017 = QtWidgets.QRadioButton(self.tab_2)
        self.op4_2017.setGeometry(QtCore.QRect(30, 130, 301, 20))
        self.op4_2017.setObjectName("op4_2017")
        self.pushButton_2017 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2017.setGeometry(QtCore.QRect(230, 180, 113, 32))
        self.pushButton_2017.setObjectName("pushButton_2017")
        self.pushButton_2017.clicked.connect(lambda: self.lectura_de_datos(2017))
        self.pushButton_2017.clicked.connect(self.generar_grafica)
        self.pushButton_2017.clicked.connect(self.generar_tabla)
        self.pushButton_2017_json = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2017_json.setGeometry(QtCore.QRect(230, 210, 113, 32))
        self.pushButton_2017_json.setObjectName("pushButton_2017_json")
        self.pushButton_2017_json.clicked.connect(lambda: self.agregar_json(2017))

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_3.setObjectName("label_3")
        self.op1_2018 = QtWidgets.QRadioButton(self.tab_4)
        self.op1_2018.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.op1_2018.setObjectName("op1_2018")
        self.op2_2018 = QtWidgets.QRadioButton(self.tab_4)
        self.op2_2018.setGeometry(QtCore.QRect(30, 70, 271, 20))
        self.op2_2018.setObjectName("op2_2018")
        self.op3_2018 = QtWidgets.QRadioButton(self.tab_4)
        self.op3_2018.setGeometry(QtCore.QRect(30, 100, 301, 20))
        self.op3_2018.setObjectName("op3_2018")
        self.op4_2018 = QtWidgets.QRadioButton(self.tab_4)
        self.op4_2018.setGeometry(QtCore.QRect(30, 130, 301, 20))
        self.op4_2018.setObjectName("op4_2018")
        self.pushButton_2018 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2018.setGeometry(QtCore.QRect(230, 180, 113, 32))
        self.pushButton_2018.setObjectName("pushButton_2018")
        self.pushButton_2018.clicked.connect(lambda: self.lectura_de_datos(2018))
        self.pushButton_2018.clicked.connect(self.generar_grafica)
        self.pushButton_2018.clicked.connect(self.generar_tabla)
        self.pushButton_2018_json = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2018_json.setGeometry(QtCore.QRect(230, 210, 113, 32))
        self.pushButton_2018_json.setObjectName("pushButton_2018_json")
        self.pushButton_2018_json.clicked.connect(lambda: self.agregar_json(2018))

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setGeometry(QtCore.QRect(10, 40, 370, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(400, 40, 370, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_reporte = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_reporte.setGeometry(QtCore.QRect(580, 350, 201, 32))
        self.pushButton_reporte.setObjectName("pushButton_reporte")
        self.pushButton_reporte.clicked.connect(self.generar_reporte)

        self.titulo = QtWidgets.QLabel(self.tab_3)
        self.titulo.setGeometry(QtCore.QRect(270, 7, 400, 15))

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 331, 281))
        self.tableWidget.setRowCount(13)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)

        self.barra1 = QtWidgets.QLabel(self.frame_2)
        self.barra1.setGeometry(QtCore.QRect(10, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra1.setFont(font)
        self.barra1.setAutoFillBackground(True)
        self.barra1.setFrameShape(QtWidgets.QFrame.Box)
        self.barra1.setLineWidth(1)
        self.barra1.setText("")
        self.barra1.setStyleSheet("QLabel {background-color: gray;}")
        self.barra1.setObjectName("barra1")
        self.nombre1 = QtWidgets.QLabel(self.frame_2)
        self.nombre1.setGeometry(QtCore.QRect(12, 280, 20, 15))

        self.barra2 = QtWidgets.QLabel(self.frame_2)
        self.barra2.setGeometry(QtCore.QRect(40, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra2.setFont(font)
        self.barra2.setAutoFillBackground(True)
        self.barra2.setFrameShape(QtWidgets.QFrame.Box)
        self.barra2.setLineWidth(1)
        self.barra2.setText("")
        self.barra2.setStyleSheet("QLabel {background-color: gray;}")
        self.barra2.setObjectName("barra2")
        self.nombre2 = QtWidgets.QLabel(self.frame_2)
        self.nombre2.setGeometry(QtCore.QRect(42, 280, 20, 15))

        self.barra3 = QtWidgets.QLabel(self.frame_2)
        self.barra3.setGeometry(QtCore.QRect(70, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra3.setFont(font)
        self.barra3.setAutoFillBackground(True)
        self.barra3.setFrameShape(QtWidgets.QFrame.Box)
        self.barra3.setLineWidth(1)
        self.barra3.setText("")
        self.barra3.setStyleSheet("QLabel {background-color: gray;}")
        self.barra3.setObjectName("barra3")
        self.nombre3 = QtWidgets.QLabel(self.frame_2)
        self.nombre3.setGeometry(QtCore.QRect(72, 280, 20, 15))

        self.barra4 = QtWidgets.QLabel(self.frame_2)
        self.barra4.setGeometry(QtCore.QRect(100, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra4.setFont(font)
        self.barra4.setAutoFillBackground(True)
        self.barra4.setFrameShape(QtWidgets.QFrame.Box)
        self.barra4.setLineWidth(1)
        self.barra4.setText("")
        self.barra4.setStyleSheet("QLabel {background-color: gray;}")
        self.barra4.setObjectName("barra4")
        self.nombre4 = QtWidgets.QLabel(self.frame_2)
        self.nombre4.setGeometry(QtCore.QRect(102, 280, 20, 15))

        self.barra5 = QtWidgets.QLabel(self.frame_2)
        self.barra5.setGeometry(QtCore.QRect(130, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra5.setFont(font)
        self.barra5.setAutoFillBackground(True)
        self.barra5.setFrameShape(QtWidgets.QFrame.Box)
        self.barra5.setLineWidth(1)
        self.barra5.setText("")
        self.barra5.setStyleSheet("QLabel {background-color: gray;}")
        self.barra5.setObjectName("barra5")
        self.nombre5 = QtWidgets.QLabel(self.frame_2)
        self.nombre5.setGeometry(QtCore.QRect(132, 280, 20, 15))

        self.barra6 = QtWidgets.QLabel(self.frame_2)
        self.barra6.setGeometry(QtCore.QRect(160, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra6.setFont(font)
        self.barra6.setAutoFillBackground(True)
        self.barra6.setFrameShape(QtWidgets.QFrame.Box)
        self.barra6.setLineWidth(1)
        self.barra6.setText("")
        self.barra6.setStyleSheet("QLabel {background-color: gray;}")
        self.barra6.setObjectName("barra6")
        self.nombre6 = QtWidgets.QLabel(self.frame_2)
        self.nombre6.setGeometry(QtCore.QRect(162, 280, 20, 15))

        self.barra7 = QtWidgets.QLabel(self.frame_2)
        self.barra7.setGeometry(QtCore.QRect(190, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra7.setFont(font)
        self.barra7.setAutoFillBackground(True)
        self.barra7.setFrameShape(QtWidgets.QFrame.Box)
        self.barra7.setLineWidth(1)
        self.barra7.setText("")
        self.barra7.setStyleSheet("QLabel {background-color: gray;}")
        self.barra7.setObjectName("barra7")
        self.nombre7 = QtWidgets.QLabel(self.frame_2)
        self.nombre7.setGeometry(QtCore.QRect(192, 280, 20, 15))

        self.barra8 = QtWidgets.QLabel(self.frame_2)
        self.barra8.setGeometry(QtCore.QRect(220, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra8.setFont(font)
        self.barra8.setAutoFillBackground(True)
        self.barra8.setFrameShape(QtWidgets.QFrame.Box)
        self.barra8.setLineWidth(1)
        self.barra8.setText("")
        self.barra8.setStyleSheet("QLabel {background-color: gray;}")
        self.barra8.setObjectName("barra8")
        self.nombre8 = QtWidgets.QLabel(self.frame_2)
        self.nombre8.setGeometry(QtCore.QRect(222, 280, 20, 15))

        self.barra9 = QtWidgets.QLabel(self.frame_2)
        self.barra9.setGeometry(QtCore.QRect(250, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra9.setFont(font)
        self.barra9.setAutoFillBackground(True)
        self.barra9.setFrameShape(QtWidgets.QFrame.Box)
        self.barra9.setLineWidth(1)
        self.barra9.setText("")
        self.barra9.setStyleSheet("QLabel {background-color: gray;}")
        self.barra9.setObjectName("barra9")
        self.nombre9 = QtWidgets.QLabel(self.frame_2)
        self.nombre9.setGeometry(QtCore.QRect(252, 280, 20, 15))

        self.barra10 = QtWidgets.QLabel(self.frame_2)
        self.barra10.setGeometry(QtCore.QRect(280, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra10.setFont(font)
        self.barra10.setAutoFillBackground(True)
        self.barra10.setFrameShape(QtWidgets.QFrame.Box)
        self.barra10.setLineWidth(1)
        self.barra10.setText("")
        self.barra10.setStyleSheet("QLabel {background-color: gray;}")
        self.barra10.setObjectName("barra10")
        self.nombre10 = QtWidgets.QLabel(self.frame_2)
        self.nombre10.setGeometry(QtCore.QRect(280, 280, 22, 15))

        self.barra11 = QtWidgets.QLabel(self.frame_2)
        self.barra11.setGeometry(QtCore.QRect(310, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra11.setFont(font)
        self.barra11.setAutoFillBackground(True)
        self.barra11.setFrameShape(QtWidgets.QFrame.Box)
        self.barra11.setLineWidth(1)
        self.barra11.setText("")
        self.barra11.setStyleSheet("QLabel {background-color: gray;}")
        self.barra11.setObjectName("barra11")
        self.nombre11 = QtWidgets.QLabel(self.frame_2)
        self.nombre11.setGeometry(QtCore.QRect(310, 280, 22, 15))

        self.barra12 = QtWidgets.QLabel(self.frame_2)
        self.barra12.setGeometry(QtCore.QRect(340, 275, 20, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.barra12.setFont(font)
        self.barra12.setAutoFillBackground(True)
        self.barra12.setFrameShape(QtWidgets.QFrame.Box)
        self.barra12.setLineWidth(1)
        self.barra12.setText("")
        self.barra12.setStyleSheet("QLabel {background-color: gray;}")
        self.barra12.setObjectName("barra12")
        self.nombre12 = QtWidgets.QLabel(self.frame_2)
        self.nombre12.setGeometry(QtCore.QRect(340, 280, 22, 15))

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Usuario: {}".format(self.usuario))

        self.actionGuardar_sesion = QtWidgets.QAction(MainWindow)
        self.actionGuardar_sesion.setObjectName("actionGuardar_sesion")
        self.actionGuardar_sesion.setShortcut("Ctrl+G")
        self.actionAbrir_sesion = QtWidgets.QAction(MainWindow)
        self.actionAbrir_sesion.setObjectName("actionAbrir_sesion")
        self.actionAbrir_sesion.setShortcut("Ctrl+A")
        self.actionSalir_del_programa = QtWidgets.QAction(MainWindow)
        self.actionSalir_del_programa.setObjectName("actionSalir_del_programa")
        self.actionSalir_del_programa.setShortcut("Ctrl+S")
        self.actionSalir_del_programa.triggered.connect(MainWindow.close)
        self.menuArchivo.addAction(self.actionGuardar_sesion)
        self.menuArchivo.addAction(self.actionAbrir_sesion)
        self.menuArchivo.addAction(self.actionSalir_del_programa)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.menubar.triggered[QtWidgets.QAction].connect(self.menu)
        
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guatecompras"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Compras 2016"))
        self.label.setText(_translate("MainWindow", "Obtener datos:"))
        self.op1_2016.setText(_translate("MainWindow", "Compras más grandes"))
        self.op2_2016.setText(_translate("MainWindow", "Compra más grande realizadas por mes"))
        self.op3_2016.setText(_translate("MainWindow", "Compras más grandes realizadas por la USAC"))
        self.op4_2016.setText(_translate("MainWindow", "Top 10 de los proveedores que más vendieron"))
        self.pushButton_2016.setText(_translate("MainWindow", "Generar"))
        self.pushButton_2016_json.setText(_translate("MainWindow", "Ingresar datos"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Compras 2017"))
        self.label_2.setText(_translate("MainWindow", "Obtener datos:"))
        self.op1_2017.setText(_translate("MainWindow", "Compras más grandes"))
        self.op2_2017.setText(_translate("MainWindow", "Compra más grande realizadas por mes"))
        self.op3_2017.setText(_translate("MainWindow", "Compras más grandes realizadas por la USAC"))
        self.op4_2017.setText(_translate("MainWindow", "Top 10 de los proveedores que más vendieron"))
        self.pushButton_2017.setText(_translate("MainWindow", "Generar"))
        self.pushButton_2017_json.setText(_translate("MainWindow", "Ingresar datos"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Compras 2018"))
        self.label_3.setText(_translate("MainWindow", "Obtener datos:"))
        self.op1_2018.setText(_translate("MainWindow", "Compras más grandes"))
        self.op2_2018.setText(_translate("MainWindow", "Compra más grande realizadas por mes"))
        self.op3_2018.setText(_translate("MainWindow", "Compras más grandes realizadas por la USAC"))
        self.op4_2018.setText(_translate("MainWindow", "Top 10 de los proveedores que más vendieron"))
        self.pushButton_2018.setText(_translate("MainWindow", "Generar"))
        self.pushButton_2018_json.setText(_translate("MainWindow", "Ingresar datos"))
        
        self.pushButton_reporte.setText(_translate("MainWindow", "Generar reporte en PDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Gráficas y análisis"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionGuardar_sesion.setText(_translate("MainWindow", "Guardar sesión"))
        self.actionAbrir_sesion.setText(_translate("MainWindow", "Abrir sesión"))
        self.actionSalir_del_programa.setText(_translate("MainWindow", "Salir del programa"))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "No."))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "NIT/NOG"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Monto"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainWindow", "12"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)