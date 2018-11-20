#-*-coding:utf8 -*-
import json
from pprint import  pprint
import pandas as pd
from pandas.io.json import json_normalize
import socket
import subprocess

class Lectura_de_Datos_json():
    def __init__(self, anio):
        if anio == 2016:
            with open("concursos_2016_terminado_adjudicado.json", "r") as archivo:
                self.datos = json.load(archivo)
        elif anio == 2017:
            with open("concursos-publicados-2017-finalizados-adjudicados.json", "r") as archivo:
                self.datos = json.load(archivo)
        else:
            with open("concursos-publicados-2018-finalizados-adjudicados.json", "r") as archivo:
                self.datos = json.load(archivo)
        
        self.df = pd.DataFrame.from_dict(json_normalize(self.datos), orient='columns')
        self.montos = self.df["MONTO"]
        self.nog_concurso = self.df["NOG CONCURSO"]
        self.descripciones = self.df["DESCRIPCIÓN"]

    def getNogConcurso(self):
        return(self.nog_concurso)
    
    def getDescripciones(self):
        return(self.descripciones)

    #El top 10 de las compras más grandes (por monto) realizada para ese año.
    def opcion1(self):
        montos_indexados = []
        i = 0
        for m in self.montos:
            try:
                #montos_indexados.append((int(m.replace('.','')), i))
                montos_indexados.append((int(m.split('.')[0]), i)) # supuestamente arreglado
                i += 1
            except ValueError:
                i += 1

        return(sorted(montos_indexados)[-10:])
    
    #La compra más grande realizadas por mes (con datos del proveedor y del contratante)
    def opcion2(self):
        meses = self.df["MES DE ADJUDICACIÓN"]
        meses_montos_indexados = [[],[],[],[],[],[],[],[],[],[],[],[]]
        tupla_meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',\
                        'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
        i = 0
        for m in meses:
            mes_m = m.replace(' ', '')
            for j in tupla_meses:
                if mes_m == j:
                    try:
                        #meses_montos_indexados[tupla_meses.index(j)].append((int(self.montos[i].replace('.','')), i))
                        meses_montos_indexados[tupla_meses.index(j)].append((int(self.montos[i].split('.')[0]), i)) # supuestamente arreglado
                        i += 1
                        break
                    except ValueError:
                        i += 1
                        break

        mas_grande_por_mes = []
        for i in meses_montos_indexados:
            try:
                mas_grande_por_mes.append(max(i))
            except ValueError:
                mas_grande_por_mes.append((0,0))
        
        return(mas_grande_por_mes)
    
    #El top 10 de las compras más grandes realizadas por la Universidad de San Carlos de Guatemala (USAC)
    def opcion3(self):
        entidad_compradora = self.df['ENTIDAD COMPRADORA']
        montos_indexados = []
        i = 0
        for e in entidad_compradora:
            if e == "UNIVERSIDAD DE SAN CARLOS DE GUATEMALA -USAC-":
                try:
                    montos_indexados.append((int(self.montos[i].replace('.','')), i))
                    #montos_indexados.append((int(self.montos[i].split('.')[0]), i)) # supuestamente arreglado
                    i += 1
                except ValueError:
                    i += 1
            else:
                i += 1
        
        return(sorted(montos_indexados)[-10:])

    #El top 10 de los proveedores(NIT) que más vendieron en ese ejercicio fiscal (por monto)
    def opcion4(self):
        nits = self.df["NIT"]
        nits_sum_montos = {}
        i = 0
        for n in nits:
            if n not in nits_sum_montos:
                try:
                    #N = int(self.montos[i].replace('.',''))
                    N = int(self.montos[i].split('.')[0]) #supuestamente arreglado
                except ValueError:
                    N = 0
                nits_sum_montos.update({n: N})
                i += 1
            else:
                try:
                    #N = nits_sum_montos.get(n) + int(self.montos[i].replace('.',''))
                    N = nits_sum_montos.get(n) + int(self.montos[i].split('.')[0]) # supuestamente arreglado
                except ValueError:
                    N = nits_sum_montos.get(n) + 0
                nits_sum_montos.update({n: N})
                i += 1

        nits_sum_montos.pop('')

        sum_montos_nits = dict(zip(nits_sum_montos.values(), nits_sum_montos.keys()))
        mayores_10_montos = sorted(sum_montos_nits)[-10:]
        mayores_10_montos_nits = []
        for i in mayores_10_montos:
            mayores_10_montos_nits.append((sum_montos_nits.get(i), i))

        return(mayores_10_montos_nits)