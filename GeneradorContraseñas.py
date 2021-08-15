import os, string, random
from random import randint

CARPETA = "Desktop/Facultad/Programación/GeneradorContraseñas/"
EXTENSION = ".txt"

def creardirectorio():
    if os.path.exists("Desktop/Facultad/Programación/GeneradorContraseñas"):
        print("Existe")
    else:
        print("No existe")
    
def existe_usuario(usuario):
    return os.path.isfile(CARPETA + usuario + EXTENSION)

def reiniciar():
    tiempo= input("Presione cualquier tecla para volver al menú principal.\n")
    os.system ("cls")        
    app()

def crear():
    usr = input("Ingrese el nombre de usuario: \n")

    #Revisar si el usuario existe
    existe = existe_usuario(usr)
    if not existe:
        desea = True
        proceder(desea, usr)
    else:
        print("El usuario ya existe, intentelo nuevamente.\n")

    reiniciar()

def proceder(desea, usr):
    print("Seleccione que desea hacer: \n")
    print("1- Introducir contraseña manualmente\n")
    print("2- Ejecutar generador de contraseñas\n")
    elec=int(input("Elección: "))
    while desea:
        if(elec == 1):
            desea = False
            contramanual(usr)

        #Ejecutar generador de contraseñas     
        elif(elec == 2):
            desea = False
            contraauto(usr)
        else:
            print("Opción incorrecta, intente nuevamente.\n")
                 
def contramanual(usr):
    valida = True
    print("=============== CONDICIONES =============\n")
    print("1- Debe tener más de 8 (ocho) digitos\n")
    print("2- Debe contener por lo menos un numero o simbolo\n")
    print("3- Debe contener por lo menos una letra mayúscula\n")
    print("=========================================\n")
    while valida:
        pwd = input("Contraseña: \n")
        count_letrasmin = len(pwd)
        count_letrasmay = sum(bool(elem.isupper()) for elem in pwd)
        count_numbers = sum(c in string.digits for c in pwd)
        count_symbols = sum(elem in '@*!#:;&_-,.$%' for elem in pwd)
        if (count_letrasmin < 8):
            print("La contraseña indicada posee menos de 8 (ocho) digitos, inténtelo nuevamente\n")
        elif (count_letrasmay < 1):
            print("Debe indicar por lo menos una letra mayúscula, inténtelo nuevamente\n")
        elif (count_numbers < 1):
            print("Debe indicar por lo menos un número, inténtelo nuevamente\n")
        elif (count_symbols < 1):
            print("Debe indicar por lo menos un símbolo, inténtelo nuevamente\n")
        else:
            valida = False
            #Crear y escribir en el archivo
            guardar(usr, pwd)

def contraauto(usr):
    print("========== GENERADOR DE CONTRASEÑAS ==========\n\n")
    count_letrasmay, count_numbers = randint(1,4)
    longitud=12
    caract=string.ascii_letters+string.digits
    while True:
        pwd=("").join(random.choice(caract)for i in range(longitud))
        if(sum(c.isupper() for c in pwd)>=count_letrasmay
            and sum(c.isdigit() for c in pwd)>=count_numbers):
            break
    print("\nSU CONTRASEÑA: ",pwd)
    guardar(usr, pwd)
    
def guardar(usr, pwd):
    with open(CARPETA + usr + EXTENSION, "w") as archivo:
        archivo.write("Usuario: " + usr + "\r\n")
        archivo.write("Contraseña: " + pwd + "\r\n")
        
        print("\r\n*** ¡Usuario creado correctamente! ***\r\n")
        accion = "crear"
        confirmacioncrear()    
 
def ver():
    archivos = os.listdir(CARPETA)   #listdir(ruta) nos permite listar los archivos de un directorio
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]   #Esto es para validar que el archivo a mostrar sea .txt
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as usuario:
            for linea in usuario:
                #Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print("\r\n")
    
    reiniciar()
    
def confirmacioncrear():
    preguntar2 = True
    while preguntar2:
        opc=input(f"¿Desea crear otro usuario? (s/n): \r\n")
        if opc == "s":
            crear()
            preguntar2 = False
        elif opc == "n":
            break
        else:
            print("Opcion incorrecta.\n")
            
def confirmacioneliminar():
    preguntar2 = True
    while preguntar2:
        opc=input(f"¿Desea eliminar otro usuario? (s/n): \r\n")
        if opc == "s":
            eliminar()
            preguntar2 = False
        elif opc == "n":
            break
        else:
            print("Opcion incorrecta.\n")

def eliminar():
    usr = input("Ingrese el nombre del usuario a buscar:\r\n")
    existe = existe_usuario(usr)
    if existe:
        preguntar1 = True
        while preguntar1:
            print("***CONTACTO ENCONTRADO***\n")
            with open(CARPETA + usr + EXTENSION) as usuario:
                #Imprimir datos
                print("===== INFORMACION DEL USUARIO ===== \r\n")
                for linea in usuario:
                    print(linea.rstrip())
                print("\r\n")

            seguro = input("¿Seguro que desea eliminar este usuario? (s/n): ")
            if seguro == "s":
                os.remove(CARPETA + usr + EXTENSION)
                print("¡Usuario eliminado con exito!\n")
                preguntar1 = False
            elif seguro == "n":
                break
            else:
                print("Opcion incorrecta. \n")
        confirmacioneliminar()
    else:
        print("No existe ningún usuario con ese nombre, inténtelo nuevamente.\n\r")

    reiniciar()

def menuprincipal():
    print("===== GESTIÓN DE CONTRASEÑAS =====\n\n")
    print("1- Crear nuevo usuario y contraseña\n")
    print("2- Ver mis usuarios y contraseñas\n")
    print("3- Eliminar usuario\n")
    print("9- Salir\r\n")  
    
def app():
    opc = 9
    elegida = True
    menuprincipal()
    while elegida:
        opc=int(input("Opción: "))
        if (opc == 1):
            crear()
            elegida = False
        elif (opc == 2):
            ver()
            elegida = False
        elif (opc == 3):
            eliminar()
            elegida = False
        elif (opc == 9):
            print("Finalizando...")
            elegida = False
        else:
            print("Opción incorrecta")
   
#Ejecucion    
app()