class Personaje():
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    
    def presentacion (self):
        print (f"hola.! mi nombre es {self.nombre}, tengo {self.edad} de edad y soy {self.ocupacion}")
    
persona1 = Personaje("angel", 30, "backend-developer")

persona1.presentacion()
