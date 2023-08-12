#las variables:
'''
las variables son referencias en memoria que nos sirven para almacenar datos
se puede decir que funcionan como cajas a las cuales guardamos un valor o un dato
al momento que invocar la variable o la caja , nos devolvera su contenido
'''
variable = 25
#para crear una variable primero tenemos que colocar un nombre, seguido del signo (=)
#el signo de asignacion (=)
#estos valores pueden ser tipo, string(cadenas de texto), numeros(enteros,flotantes o decimales), o booleanos(True: verdadero, False: falso)
#las variables pueden ser mostradas en consola con un print

numero = 1
print (numero)

numero_decimal = 1,5
print (numero_decimal)

strings = "cadena de texto"
print (strings)

boleanos = True
print (boleanos)

#type(): para conocer el tipo de una variable podemos usar el operador type()
# para visualizarlo lo podemos usar con un print, y dentro de los parentesis dle operador
#escirbir la variable
print (type(numero))
print (type(numero_decimal))
print (type(strings))
print (type(boleanos))

#podemos tambien hacer reasignacion de variables reemplazando el valor que tienen por otro nuevo

strings = "mi nombre"
print (strings)
#tambien podemos combinar variables con string dentro de un print con un Format o 
#usando el signo de mas (+)
# eso se conoce como concatenacion ejemplo :
strings = "nombre completo"
print ("aqui hicimos otro cambio de la variable " + strings) #concatenando con (+)
print (f"se necesita su {strings}") #aqui concatenamos con Format

#hasta ahora se han asignado el valor de las variables pero tambien podemos lograr
#que un usuario que pueda asignar un valor o dato
#input() este operador se usa para asignar de manera dinamica un valor desde la terminal
nombre = input("cual es tu nombre? >> ")
print (f"hola {nombre} bienvenido  ")




