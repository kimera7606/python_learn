#podemos manejar las exepciones para que estas no detengan nuestros programas
'''
podemos hacerlo con el uso de la palabra clave  Try: capturamos la logica en ese bloque
lo que quiere decir es intentar hacer algo, luego de la lofica se debe
colocar un except y dar informaicon de ese error sin para nuestro programa
'''
try:
    print (2/0)
except ZeroDivisionError as error:
    print (error)
    
print("hola, continue a pesar del error")

#podemos meter diferentes tipos de errores en toda una logica

try: #intentamos
    print(25/0) #imprimir con zero
    print(variable) #imprmir una variable que no existe
    age = 10
    if age < 18:
        raise Exception("no se aceptan menores de edad") #generar una excepcion
    numeros = iter(range(1,2)) #crear un iterable
    print(next(numeros))
    print(next(numeros))
    print(next(numeros)) #ir mas alla del limite del iterador

except ZeroDivisionError as error: #se generan los errores posibles
    print(error)
except NameError as error :
    print(error)
except AssertionError as error:
    print(error)
except StopIteration as error:
    print(error)
except:
    print("ups! ha ocurrido un error!") # personalizamos un error
'''
al final solo se mostrara le primer error encontrado , escalara de arriba a abajo
una vez choque con un error traera la exepcion y solo tomara una 
'''
print("segui continuando a pesar de los errores")
