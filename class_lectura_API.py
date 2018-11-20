from urllib.request import urlopen
import json
from pprint import  pprint
import pandas as pd
from pandas.io.json import json_normalize

class Lectura_de_Datos_API():
    def __init__(self, anio):
        if anio == 2016:
            url = 'https://datos.minfin.gob.gt/api/3/action/datastore_search?resource_id=3162c17b-1c31-41c3-bab5-fadf9b296b1a&limit=92961&fields=%22NIT%22,%22NOG%20CONCURSO%22,%22MONTO%22,%22DESCRIPCI%C3%93N%22,%22MES%20DE%20ADJUDICACI%C3%93N%22,%22ENTIDAD%20COMPRADORA%22'
        elif anio == 2017:
            url = 'https://datos.minfin.gob.gt/api/3/action/datastore_search?resource_id=ffa8c4b2-6736-49a1-855e-ba0e7caa0f34&limit=76879&fields=%22NIT%22,%22NOG%20CONCURSO%22,%22MONTO%22,%22DESCRIPCI%C3%93N%22,%22MES%20DE%20ADJUDICACI%C3%93N%22,%22ENTIDAD%20COMPRADORA%22'
        else:
            url = 'https://datos.minfin.gob.gt/api/3/action/datastore_search?resource_id=29e38c4a-74ee-44b0-a4bb-e40259f89400&limit=65738&fields=%22NIT%22,%22NOG%20CONCURSO%22,%22MONTO%22,%22DESCRIPCI%C3%93N%22,%22MES%20DE%20ADJUDICACI%C3%93N%22,%22ENTIDAD%20COMPRADORA%22'
        
        json_obj = urlopen(url)
        data = json.load(json_obj)
        datos = data['result']['records']

        self.df = pd.DataFrame.from_dict(json_normalize(datos), orient='columns')
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
                montos_indexados.append((int(m.split('.')[0]), i))
                i += 1
            except Exception:
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
                        meses_montos_indexados[tupla_meses.index(j)].append((int(self.montos[i].split('.')[0]), i))
                        i += 1
                        break
                    except Exception:
                        i += 1
                        break

        mas_grande_por_mes = []
        for i in meses_montos_indexados:
            try:
                mas_grande_por_mes.append(max(i))
            except Exception:
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
                    montos_indexados.append((int(self.montos[i].split('.')[0]), i))
                    i += 1
                except Exception:
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
                    N = int(self.montos[i].split('.')[0])
                except Exception:
                    N = 0
                nits_sum_montos.update({n: N})
                i += 1
            else:
                try:
                    N = nits_sum_montos.get(n) + int(self.montos[i].split('.')[0])
                except Exception:
                    N = nits_sum_montos.get(n) + 0
                nits_sum_montos.update({n: N})
                i += 1
        
        try:
            nits_sum_montos.pop('')
        except Exception:
            None

        sum_montos_nits = dict(zip(nits_sum_montos.values(), nits_sum_montos.keys()))
        mayores_10_montos = sorted(sum_montos_nits)[-10:]
        mayores_10_montos_nits = []
        for i in mayores_10_montos:
            mayores_10_montos_nits.append((sum_montos_nits.get(i), i))

        return(mayores_10_montos_nits)

# prueba = Lectura_de_Datos_API(2018)
# print(prueba.opcion1())