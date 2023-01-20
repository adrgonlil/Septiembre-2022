from collections import namedtuple, defaultdict
from datetime import date, datetime, timedelta
import csv
from parsers import *

Reparacion = namedtuple('Reparacion', 'numero_ref,centro,fecha_entrada,fecha_reparacion,\
numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion')

def lee_reparaciones(fichero):
    with open (fichero, encoding="utf-8") as f:
        lector=csv.reader(f, delimiter=";")
        res = []
        next(lector)
        for numero_ref,centro,fecha_entrada,fecha_reparacion,\
            numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion in lector:
            fecha_entrada=parsea_fecha(fecha_entrada)
            fecha_reparacion=parsea_fecha(fecha_reparacion)
            fecha_compra=parsea_fecha(fecha_compra)
            precio_reparacion=float(precio_reparacion)
            res.append(Reparacion(numero_ref,centro,fecha_entrada,fecha_reparacion,\
                numero_serie,tipo,descripcion_problema,fecha_compra,precio_reparacion))
    return res

def calcula_recaudacion(reparaciones, centro, tipo):
    recaudacion=0
    for r in reparaciones:
        if r.centro==centro and r.tipo==tipo or tipo==None:
            if r.fecha_compra.date()<date(2022,1,1) and r.fecha_compra.date()+timedelta(730)>r.fecha_entrada.date():
                recaudacion+=r.precio_reparacion
            elif r.fecha_compra.date()>=date(2022,1,1) and r.fecha_compra.date()+timedelta(1095)>r.fecha_entrada.date():
                recaudacion+=r.precio_reparacion
    return recaudacion

def dias_reparacion(r): 
    return (r.fecha_reparacion - r.fecha_entrada).days

def reparaciones_mas_largas(reparaciones, anyo, n, centro=None):
    lista = []
    for r in reparaciones:
        if centro==r.centro or centro is None:
            if r.fecha_entrada.year==anyo:
                lista.append((r.numero_ref, dias_reparacion(r)))
    return sorted(lista, reverse=True, key=lambda x:x[1])[:n]

                            
def centro_mas_rapido(reparaciones, centros):
    dicc=defaultdict(list)
    for r in reparaciones:
        if r.centro in centros:
            dicc[r.centro].append(dias_reparacion(r))
    for centro, tiempo in dicc.items():
        dicc[centro]=sum(tiempo)/len(tiempo)
    return min(dicc.items(), key=lambda x:x[1])[0]

def centros_experimentados_en(reparaciones, palabras): 