#Importacion de funciones
import os

#Carpeta de Contactos
CARPETA = "contactos/"  #Se pone todo en mayuscula para indicar que es una constante
EXTENSION = ".txt"  #Extension de los archivos

#Clase de Contactos
class Contacto:
    def __init__(self, nombre, numero, categoria):
        self.nombre = nombre
        self.numero = numero
        self.categoria = categoria

def crear_directorio():
    if not os.path.exists("contactos/"):    #Si una carpeta no existe entonces...
        os.makedirs("contactos/")   #Crear la carpeta

def mostrar_menu():
    
    print("======== MENU PRINCIPAL ======== \n\n")
    print("1) Agregar Nuevo Contacto\n")
    print("2) Editar Contacto\n")
    print("3) Ver Contactos\n")
    print("4) Buscar Contacto\n")
    print("5) Eliminar Contacto\n")
    print("0) Salir\n")

def agregar_contacto():
    nombre_contacto = input("Nombre del Contacto:\r\n")

    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
        
        #Resto de datos
            numero_contacto = input("Numero de Telefono:\r\n")
            categoria_contacto = input("Categoría del Contacto:\r\n")

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, numero_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Numero: " + contacto.numero + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

            #Mensaje de exito
            print("\r\n*** ¡Contacto creado correctamente! ***\r\n")
            preguntar2 = True
            while preguntar2:
                opc=input("¿Desea crear otro contacto? (s/n): \r\n")
                if opc == "s":
                    agregar_contacto()
                    preguntar2 = False
                elif opc == "n":
                    break
                else:
                    print("Opcion incorrecta.\n")
    else:
        print("Ya existe un contacto con ese nombre\n")

    #Reiniciar app
    tiempo=input("Presione cualquier tecla para salir.\n")
    os.system ("cls")        
    app()

def editar_contacto():
    nombre_anterior = input("Ingrese el nombre del contacto a editar:\r\n")

    #Revisar si el contacto existe
    existe = existe_contacto(nombre_anterior)
    if existe:
        print("***CONTACTO ENCONTRADO***\n")
        with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:

            #Resto de los datos
            nombre_contacto = input("Ingrese el nuevo nombre del contacto: \r\n")
            numero_contacto = input("Ingrese el nuevo numero de telefono:\r\n")
            categoria_contacto = input("Ingrese la nueva categoria del contacto:\r\n")

            #Instanciar
            contacto = Contacto(nombre_contacto, numero_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write("Nombre: " + contacto.nombre + "\r\n")
            archivo.write("Numero: " + contacto.numero + "\r\n")
            archivo.write("Categoría: " + contacto.categoria + "\r\n")

        #Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

        #Mensaje de exito
        print("\r\n*** ¡Contacto editado correctamente! ***\r\n")
        preguntar2 = True
        while preguntar2:
            opc=input("¿Desea editar otro contacto? (s/n): \r\n")
            if opc == "s":
                editar_contacto()
                preguntar2 = False
            elif opc == "n":
                break
            else:
                print("Opcion incorrecta.\n")
    else:
        print("Lo sentimos, el contacto ingresado no existe en la agenda\n")
    
    #Reiniciar app
    tiempo=input("Presione cualquier tecla para salir.\n")
    os.system ("cls")        
    app()

def ver_contactos():
    archivos = os.listdir(CARPETA)   #listdir(ruta) nos permite listar los archivos de un directorio
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]   #Esto es para validar que el archivo a mostrar sea .txt
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print("\r\n")
    
    #Reiniciar app
    tiempo=input("Presione cualquier tecla para salir.\n")
    os.system ("cls")        
    app()

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar:\r\n")
    existe = existe_contacto(nombre)
    if existe:
        print("***CONTACTO ENCONTRADO***\n")
        with open(CARPETA + nombre + EXTENSION) as contacto:
            #Imprimir datos
            print("===== INFORMACION DEL CONTACTO ===== \r\n")
            for linea in contacto:
                print(linea.rstrip())
            print("\r\n")

            #Dar opciones al usuario
            preguntar = True
            print("1- Editar datos\n")
            print("2- Eliminar contacto\n")
            print("3- Buscar otro contacto\n")
            print("0- Volver al menú principal\n")
            while preguntar:
                opc=input("Opción: \r\n")
                opc = int(opc)
                if opc == 1:
                    editar_contacto()
                    preguntar = False
                elif opc == 2:
                    eliminar_contacto()
                    preguntar = False
                elif opc == 3:
                    buscar_contacto()
                    preguntar = False
                elif opc == 0:
                    break
                else:
                    print("Opción no válida, inténtelo nuevamente.")
                    break
    else:
        print("El contacto ingresado no existe.\r\n")
    
    #Reiniciar app
    tiempo=input("Presione cualquier tecla para salir.\n")
    os.system ("cls")        
    app()

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar:\r\n")
    existe = existe_contacto(nombre)
    if existe:
        preguntar1 = True
        while preguntar1:
            print("***CONTACTO ENCONTRADO***\n")
            with open(CARPETA + nombre + EXTENSION) as contacto:
                #Imprimir datos
                print("===== INFORMACION DEL CONTACTO ===== \r\n")
                for linea in contacto:
                    print(linea.rstrip())
                print("\r\n")

            seguro = input("¿Seguro que desea eliminar este contacto? (s/n): ")
            if seguro == "s":
                os.remove(CARPETA + nombre + EXTENSION)
                print("¡Contacto eliminado con exito!\n")
                preguntar1 = False
            elif seguro == "n":
                break
            else:
                print("Opcion incorrecta. \n")
        preguntar2 = True
        while preguntar2:
            opc=input("¿Desea eliminar otro contacto? (s/n): \r\n")
            if opc == "s":
                eliminar_contacto()
                preguntar2 = False
            elif opc == "n":
                break
            else:
                print("Opcion incorrecta.\n")
    else:
        print("No existe ningún contacto con ese nombre, inténtelo nuevamente.\n\r")

    #Reiniciar app
    tiempo=input("Presione cualquier tecla para salir.\n")
    os.system ("cls")        
    app()

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()

    #Menu de opciones
    mostrar_menu()

    #Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input("Opción: \n")
        opcion = int(opcion)

    #Ejecutar opciones
        if opcion == 1:
            print("Opción seleccionada: 1) Agregar Nuevo Contacto\n\n")
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print("Opción seleccionada: 2) Editar Contacto\n")
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            print("Opción seleccionada: 3) Ver Contactos\n")
            ver_contactos()
            preguntar = False
        elif opcion == 4:
            print("Opción seleccionada: 4) Buscar Contacto\n")
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            print("Opción seleccionada: 5) Eliminar Contacto\n")
            eliminar_contacto()
            preguntar = False
        elif opcion == 0:
            print("Finalizando...\n")
            preguntar = False
        else:
            print("Opción no válida, intentelo nuevamente\n")

#Ejecución
app()