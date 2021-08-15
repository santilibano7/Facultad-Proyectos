#Clases

class Clases:
    class Restaurant: #Primera letra de la clase tiene que ser mayuscula

        def agregar_restaurant(self, nombre): #se le pasa self al declarar, pero cuando se llama no
            self.nombre = nombre #Atributo
            print("Agregando...")

        def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}")

    #Instanciar la clase
    restaurant = Restaurant()
    restaurant.agregar_restaurant("Pizzeria Los Hijos de Puta") #mandar a llamar un metodo especifico
    restaurant.mostrar_informacion()

    restaurant2 = Restaurant() #se crea un segundo objeto, con las mismas funciones pero con distintos datos
    restaurant2.agregar_restaurant("Hamburguesas Puto")
    restaurant2.mostrar_informacion()

    #Mostrar la informacion (otra forma)
    print(f"Nombre Restaurant: {restaurant.nombre}")
    print(f"Nombre Restaurant: {restaurant2.nombre}")

    print("\n\n\n*************************************\n\n\n")

#Constructores, Abstraccion y Encapsulamiento

class ConsAbsyEnc:
    class Restaurant:

        def __init__(self, nombre, categoria, precio): #Esto es un CONSTRUCTOR, se manda a llamar automaticamente
            print("Yo me mando a llamar automaticamente")
            #Paso el procedimiento agregar_restaurant al constructor
            self.nombre = nombre
            self.categoria = categoria
            self._precio = precio
            #Para prevenir que no se pueda cambiar el precio como se hace en las lineas 48 y 53, se debe
            #encapsular, por default las variables de arriba son PUBLICAS, para hacerlas PROTECTED se 
            #les agrega un _ antes (self._precio = precio), y para hacerlas PRIVATE se agrega doble __
            print("Agregando...")

        def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self._precio}")

    #Instanciar la clase
    restaurant = Restaurant("Pizzeria Los Hijos de Puta", "Comida Italiana", 50) #Se pasa al constructor
    print(restaurant._precio)
    restaurant._precio = 80 #Una forma de cambiarle el precio
    restaurant.mostrar_informacion()

    restaurant2 = Restaurant("Hamburguesas Puto", "Comida Rapida", 100)
    print(restaurant2._precio)
    restaurant2._precio = 200 #Si ._precio fuera PRIVATE, no se podria modificar
    restaurant2.mostrar_informacion()

    print("\n\n\n*************************************\n\n\n")

#Getters y Setters

class GetySet:

    class Restaurant:

        def __init__(self, nombre, categoria, precio):
            print("Yo me mando a llamar automaticamente")
            self.nombre = nombre
            self.categoria = categoria
            self.__precio = precio
            print("Agregando...")

        def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}")

        #Definicion de GETTERS y SETTERS
        #Estos se utilizan para obtener y modificar valores que son PRIVATE

        def get_precio(self):      #GET obtiene un valor, en este caso precio
            print(f"Precio modificado con set_precio: {self.__precio}")

        def set_precio(self, precio): #SET agrega un valor
            self.__precio = precio

    restaurant = Restaurant("Pizzeria Los Hijos de Puta", "Comida Italiana", 50)
    #restaurant.__precio = 80 No se puede modificar asi ya que ahora es PRIVATE
    restaurant.mostrar_informacion()
    restaurant.set_precio(100)
    restaurant.get_precio()

    restaurant2 = Restaurant("Hamburguesas Puto", "Comida Rapida", 100)
    #restaurant2.__precio = 200 No se puede modificar asi ya que ahora es PRIVATE
    restaurant2.mostrar_informacion()
    restaurant2.set_precio(200)
    restaurant2.get_precio()

    print("\n\n\n*************************************\n\n\n")

#Herencia

class Herencia:
    class Restaurant:

        def __init__(self, nombre, categoria, precio):
            print("Yo me mando a llamar automaticamente")
            self.nombre = nombre
            self.categoria = categoria
            self.__precio = precio
            print("Agregando...")

        def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}")

        def get_precio(self):
            print(f"Precio modificado con set_precio: {self.__precio}")

        def set_precio(self, precio):
            self.__precio = precio

    #Crear una clase hijo de Restaurant
    class Hotel(Restaurant): #En el () se pone de que clase va a heredar los metodos

        def __init__(self, nombre, categoria, precio):  #Se pasan los parametros al ()
            super().__init__(nombre, categoria, precio) #Con super() hacemos referencia a la clase padre

    hotel = Hotel("Hotel APP", "5 Estrellas", 200) #Hereda nombre, categoria y precio
    hotel.mostrar_informacion()
    hotel.set_precio(1000)
    hotel.get_precio()

    print("\n\n\n*************************************\n\n\n")

#Polimorfismo

class Polimorfismo:
    class Restaurant:

        def __init__(self, nombre, categoria, precio):
            print("Yo me mando a llamar automaticamente")
            self.nombre = nombre
            self.categoria = categoria
            self.precio = precio
            print("Agregando...")

        def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")

        def get_precio(self):
            print(f"Precio modificado con set_precio: {self.precio}")

        def set_precio(self, precio):
            self.precio = precio

    class Hotel(Restaurant):

        def __init__(self, nombre, categoria, precio, segundopiso): #se agrega aca, no en la clase padre
            super().__init__(nombre, categoria, precio)
            self.segundopiso = segundopiso

        #Agregar un metodo que solo exista en hotel (otra forma de POLIMORFISMO)
        def get_segundopiso(self):
            print(self.segundopiso)

        #Reescribir un metodo (debe llamarse IGUAL) (otra forma de POLIMORFISMO)
        def mostrar_informacion(self):
            print(f"Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Tiene segundo piso: {self.segundopiso}")


        #Si queremos agregar un atributo nuevo a Hotel, tipo si tiene segundo piso o no
        #esa es una forma de POLIMORFISMO
    hotel = Hotel("Hotel APP", "5 Estrellas", 200, "Si")
    hotel.mostrar_informacion()
    hotel.set_precio(1000)
    hotel.get_precio()
    hotel.get_segundopiso()

    print("\n\n\n*************************************\n\n\n")