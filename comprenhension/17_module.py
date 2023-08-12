#los modulos nos permiten encerrar la logica para poderlo usar en otros archivos
#ejemplos
import sys # system: es para preguntar sobre el sistema operativo
print(sys.path) #imprime la ubicacion del sistema donde se esta ejecutando el archivo py

import re #expreisones regulares
text = "mi numero de telefono es 04246757606, el codigo del pais es +57"
#con una expresion regular podemos extraer los numero del texto
result = re.findall("[0-9]+", text) #buscar numeros de 0-9
print(result)

import time #manejo de tiempo, hora y fecha
tiempo = time.time() #contadro de segundos
local = time.localtime() #hora local en computadora
horita = time.asctime() #hora local humanos
print(tiempo)
print(local)
print(horita)

import collections #es una utilidad para manejar listas
numbers = [1,2,56,4,6,25,13,21,2,13,21,321,65,465,4,21,321,21,2,1,321,2,1,3]
counter = collections.Counter(numbers) #nos devolvera un diccionario con la frecuencia
#de cada dato
print(counter)

