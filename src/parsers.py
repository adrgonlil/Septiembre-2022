from datetime import datetime

def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y")
    