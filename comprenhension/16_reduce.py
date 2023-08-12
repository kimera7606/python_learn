#reduce listas o estructuras de datos iterables a un solo valor
#reduce debe ser importada de FUNCTOOLS 
from functools import reduce
from random import randint
numbers = [i * randint(2,9) for i in range(1,20)]
print(numbers)

resultado = reduce(lambda counter, item : counter + item, numbers)
print(resultado)
resultado2 = sum(numbers)
print(resultado2)