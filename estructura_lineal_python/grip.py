from array_1 import Array

class Grid():
    def __init__(self, filas, columnas, valor = None):
        self.data = Array(columnas, valor)
        for fila in range(filas):
            self.data[fila] = Array(columnas, valor)
    
    def get_altura(self):
        return len(self.data)
    
    def get_ancho(self):
        return len(self.data[0])
    
    def __get__ (self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        for fila in range(self.get_altura()):
            for col in range(self.get_ancho):
                result += str(self.data[fila][col]) + " "
                
            result += "\n"
        
        return str(result)
