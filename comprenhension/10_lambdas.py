#LAMBDA
'''
son funciones que tienen una sintaxis sencilla y directa
'''
#ejemplo de una funcion que incrementa un numero
def incremento (number): #se crea la funcion que pide un parametro number
    return number + 10 # se retorna el numero + 10
print(incremento(10))

#lambda

incremento = lambda x : x + 10 #aqui realizamos un parametro con una lambda
print(incremento(10)) #imprmimos la funcion y entre parentesis el parametro

#las lambdas pueden recibier varios parametro separados con comas
def suma1 (a,b):
    return a+b
print(suma1(50,50))

suma2 = lambda a,b : a +b
print(suma2(30,30))
