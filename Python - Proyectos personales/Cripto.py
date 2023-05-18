import os, string

CARPETA = "cripto/"
EXTENSION = ".txt"

class Cripto:
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        
def crear_directorio():
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)
        
def mostrar_menu(): 
    print("======== MENU PRINCIPAL ======== \n\n")
    print("1) Registrar nueva transacción\n")
    print("2) Editar transacción\n")
    print("3) Ver historial de transacciones\n")
    print("4) Buscar transacción\n")
    print("5) Eliminar transacción\n")
    print("6) Ver mi billetera\n")
    print("0) Salir\n")
    
def registrar_transaccion():
    coin = input("Nombre de la criptomoneda: \r\n")