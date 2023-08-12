#high orden function es cuando colocamos una funcion como parametro en otra function
def incremento (number):
    return number + 1

def high_order_function(number,function):
    return number + function(number)

resultado = high_order_function(2, incremento)
print(resultado)

## versiones lambda 

sumitaSimple = lambda x : x +1
sumita_hof = lambda x,funct : x + funct(x)
resultado2 = sumita_hof(10,sumitaSimple) 