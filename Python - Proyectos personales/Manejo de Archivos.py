def FuncionesUno():
    
    #Crear un archivo

    archivo = open("archivo.txt", "w")
    #archivo = open("nombredelarchivo.formato", "modo/permisos")
    #OPEN es una funcion de Python para crear archivos
    #W (o Write) es archivo o permiso de escritura

    #Generar numeros en el archivo
    for i in range(0, 20):
        archivo.write("Esta es la linea " + str(i+1) + "\n\r")

    #Cerrar el archivo
    archivo.close()

def FuncionesDos():
    
    #Esto abre, lee el archivo.txt y sus datos, y los despliega en el terminal, y lo cierra
    with open("archivo.txt") as archivo:    #por default se abre en modo R (Read/Lectura)
        for contenido in archivo:
            print(contenido.rstrip()) #el rstrip() sirve para eliminar los saltos de linea en el terminal

FuncionesUno()
FuncionesDos()