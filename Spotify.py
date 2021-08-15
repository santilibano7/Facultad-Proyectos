#Importacion de funciones
import os

#Carpeta de Canciones
CARPETAPLAYLISTS = "playlists/"
EXTENSION = ".txt"  #Extension de los archivos

#Clase de Canciones
class Canciones:
    def __init__(self, titulo_cancion, artista_cancion, album_cancion, genero_cancion, duracion_cancion):
        self.titulo_cancion = titulo_cancion
        self.artista_cancion = artista_cancion
        self.album_cancion = album_cancion
        self.genero_cancion = genero_cancion
        self.duracion_cancion = duracion_cancion

def crear_directorio(): #Hecho
    if not os.path.exists("playlists/"):    #Si una carpeta no existe entonces...
        os.makedirs("playlists/")   #Crear la carpeta

def mostrar_menu(): #Hecho
    
    print("======== MENU PRINCIPAL SPOTIFY ======== \n\n")
    print("1) Crear Nueva Playlist\n")
    print("2) Agregar/Eliminar Canciones de una Playlist\n")
    print("3) Editar Datos de una Playlist\n")
    print("4) Ver mis Playlists\n")
    print("5) Buscar Playlist\n")
    print("6) Eliminar Playlist\n")
    print("0) Salir\n")

def crear_playlist():   #Hecho
    nombre_playlist = input("Ingrese un Nombre para la Playlist:\r\n")

    if not os.path.exists(f"playlists/{nombre_playlist}/"):
        os.makedirs(f"playlists/{nombre_playlist}/")   #Crear la carpeta

        _extracted_from_crear_playlist_7(
            "\r\n*** ¡Playlist creada correctamente! ***\r\n"
        )

    else:
        _extracted_from_crear_playlist_7("Ya existe una playlist con ese nombre\n")
    #Reiniciar app
    tiempo=input("Presione cualquier tecla para salir.\n")
    os.system ("cls")
    app()

def _extracted_from_crear_playlist_7(arg0):
    print(arg0)
    preguntar1 = True
    while preguntar1:
        opc=input("¿Desea crear otra playlist? (s/n): \r\n")
        if opc == "s":
            crear_playlist()
            preguntar1 = False
        elif opc == "n":
            break
        else:
            print("Opcion incorrecta.\n")

def ver_playlists():    #Hecho
    archivos = os.listdir(CARPETAPLAYLISTS)
    print("MIS PLAYLISTS:\n\r")
    print(archivos)

def agreli_playlist():
    ver_playlists()
    nombre_playlist = input("Ingrese el nombre de la playlist: \r\n")
    if os.path.exists(f"playlists/{nombre_playlist}/"):
        preguntar1 = True
        if not os.listdir(f"playlists/{nombre_playlist}/"): #Si la playlist está vacia, agregar automaticamente
            titulo_cancion = input("Titulo de la Cancion:\r\n")
            with open(f"playlists/{nombre_playlist}/" + titulo_cancion + EXTENSION, "w") as archivo:
                
                _extracted_from_agreli_playlist_11(titulo_cancion, archivo)
            #Reiniciar app
            tiempo=input("Presione cualquier tecla para salir.\n")
            os.system ("cls")
            app()
        else:
            print("===== CANCIONES DE LA PLAYLIST =====\n")
            os.listdir(f"playlists/{nombre_playlist}/")
            while preguntar1:
                print("1- Agregar Canciones\r\n")
                print("2- Eliminar Canciones\r\n")
                print("0- Volver al Menu Principal\r\n")
                opc=input("Opción: \r\n")
                opc=int(opc)
                if opc == 0:
                    break
                elif opc == 1:
                    titulo_cancion = input("Titulo de la Cancion:\r\n")
                    with open(f"playlists/{nombre_playlist}/" + titulo_cancion + EXTENSION, "w") as archivo:
                    #Resto de datos
                        artista_cancion = input("Artista de la Cancion:\r\n")
                        album_cancion = input("Album de la Cancion:\r\n")
                        genero_cancion = input("Genero de la Cancion:\r\n")
                        duracion_cancion = input("Duracion en segundos de la Cancion:\r\n")

                        #Instanciar la clase
                        canciones = Canciones(titulo_cancion,artista_cancion,album_cancion,genero_cancion,duracion_cancion)

                        #Escribir en el archivo
                        archivo.write("Titulo: " + canciones.titulo_cancion + "\r\n")
                        archivo.write("Artista: " + canciones.artista_cancion + "\r\n")
                        archivo.write("Album: " + canciones.album_cancion + "\r\n")
                        archivo.write("Genero: " + canciones.genero_cancion + "\r\n")
                        archivo.write("Duracion: " + canciones.duracion_cancion + "\r\n")
                        #Mensaje de exito
                        print("\r\n***  Cancion agregada correctamente! ***\r\n")

                    #Reiniciar app
                    tiempo=input("Presione cualquier tecla para salir.\n")
                    os.system ("cls")
                    app()

                elif opc == 2:
                    titulo_cancion = input("Titulo de la Cancion a Eliminar:\r\n")
                    existe = existe_cancion(titulo_cancion,nombre_playlist)
                    if existe:
                        preguntar1 = True
                        while preguntar1:
                            with open(f"playlists/{nombre_playlist}/" + titulo_cancion + EXTENSION, "w") as archivo:
                                #Imprimir datos
                                print("===== INFORMACION DE LA CANCION ===== \r\n")
                                for linea in archivo:
                                    print(linea.rstrip())
                                print("\r\n")

                            seguro = input("¿Seguro que desea eliminar esta canción? (s/n): ")
                            if seguro == "s":
                                os.remove(f"playlists/{nombre_playlist}/" + titulo_cancion + EXTENSION)
                                print("¡Canción eliminada con exito!\n")
                                preguntar1 = False
                            elif seguro == "n":
                                break
                            else:
                                print("Opcion incorrecta. \n")
                    else:
                        print("No existe ninguna canción con ese nombre, inténtelo nuevamente.\n\r")

                    #Reiniciar app
                    tiempo=input("Presione cualquier tecla para salir.\n")
                    os.system ("cls")
                    app()
                else:
                    print("Opcion incorrecta.\n")
    else:
        print("No existe una playlist con ese nombre\n")
        preguntar2 = True
        while preguntar2:
            opc=input("¿Desea seleccionar otra playlist? (s/n): \r\n")
            if opc == "s":
                agreli_playlist()
                preguntar2 = False
            elif opc == "n":
                break
            else:
                print("Opcion incorrecta.\n")

def _extracted_from_agreli_playlist_11(titulo_cancion, archivo):
                #Resto de datos
    artista_cancion = input("Artista de la Cancion:\r\n")
    album_cancion = input("Album de la Cancion:\r\n")
    genero_cancion = input("Genero de la Cancion:\r\n")
    duracion_cancion = input("Duracion en segundos de la Cancion:\r\n")

    #Instanciar la clase
    canciones = Canciones(titulo_cancion,artista_cancion,album_cancion,genero_cancion,duracion_cancion)

    #Escribir en el archivo
    archivo.write("Titulo: " + canciones.titulo_cancion + "\r\n")
    archivo.write("Artista: " + canciones.artista_cancion + "\r\n")
    archivo.write("Album: " + canciones.album_cancion + "\r\n")
    archivo.write("Genero: " + canciones.genero_cancion + "\r\n")
    archivo.write("Duracion: " + canciones.duracion_cancion + "\r\n")
    #Mensaje de exito
    print("\r\n***  Cancion agregada correctamente! ***\r\n")

def existe_cancion(titulo_cancion, nombre_playlist):
    return os.path.isfile(f"playlists/{nombre_playlist}/")

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
        if opcion == 0:
            print("Finalizando...\n")
            preguntar = False
        elif opcion == 1:
            print("Opción seleccionada: 1) Crear Nueva Playlist\n\n")
            crear_playlist()
            preguntar = False
        elif opcion == 2:
            print("Opción seleccionada: 2) Agregar/Eliminar Canciones de una Playlist\n")
            agreli_playlist()
            preguntar = False
        elif opcion == 3:
            print("Opción seleccionada: 3) Editar Datos de una Playlist\n")
            editar_playlist()
            preguntar = False
        elif opcion == 4:
            print("Opción seleccionada: 4) Ver mis Playlists\n")
            ver_playlists()
            preguntar = False
        elif opcion == 5:
            print("Opción seleccionada: 5) Buscar Playlist\n")
            buscar_playlist()
            preguntar = False
        elif opcion == 6:
            print("Opción seleccionada: 5) Eliminar Playlist\n")
            eliminar_playlist()
            preguntar = False
        else:
            print("Opción no válida, intentelo nuevamente\n")

#Ejecución
app()