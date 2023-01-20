from reparaciones import *

def muestra_iterable(iterable):
    for elem in iterable:
        print(elem)

def test_lectura(datos):
    print("Hay", len(datos), "datos")
    print("Estos son los dos primeros datos: \n")
    muestra_iterable(datos[:2])
    print()

def test_calcula_recaudacion(datos):
    print("Test funcion calcula recaudaciones:","\n")
    print("Recaudacion en sevilla en reparacion de portátiles:", calcula_recaudacion(datos, centro="Sevilla", tipo="portátil"))
    print()

def test_reparaciones_mas_largas(datos):
    print("Test de la funcion reparaciones mas largas:","\n")
    print(reparaciones_mas_largas(datos, 2020, 3, centro=None))

def test_centro_mas_rapido(lista): 
    print("\nTest de la función test_centro_mas_rapido") 
    print( 
        "\tCentro más rápido entre Sevilla, Huelva y Cádiz:", 
        centro_mas_rapido(lista, {"Sevilla", "Huelva", "Cádiz"}), 
    )


if __name__ == "__main__":
    reparaciones=lee_reparaciones("data/reparaciones.csv")
    test_lectura(reparaciones)
    test_calcula_recaudacion(reparaciones)
    test_reparaciones_mas_largas(reparaciones)
    test_centro_mas_rapido(reparaciones)