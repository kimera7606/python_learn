#los errores al aparecer en nuestros programas, detienen la ejecucion
'''
estos errores se pueden controlar
'''
#aqui ejecutaremos dos variables que nos daran error, pero las controlaremos
#con una exepcion
try:
    print (2/0) #por ejemplo ZeroDivisionError que es cuando dividimos en 0
    print (variable) #nameError es cuando intentamos usar una variable que no existe
except :
    print ("error")

suma = lambda a,b : a+b
assert suma(2,2 == 4) #assert solo verifica que una function trabaje de manera correcta
#peor existen otro metodos mejores para manejar errore unitarios

#podemos crear nuestras propias excepciones lo que hara que el programa se detenga
edad = 10 #creamos una variable edad con un valor de 10
if edad < 18: #creamos una condiciona en la cual si edad es menor a 18
    raise Exception("no se permiten menores de edad") #lanzara un excepcion
'''
veamos la sintaxis, primero escirbimimos RAISE seguido de la palabra 
Exception con la primera E mayuscula y entre parentesis escribimos la info 
de excepcion
'''
#recuerda que lanzar un exepcion detendra el programa.
