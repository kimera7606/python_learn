#iterables , se controlan manualmente desde el codigo
#ejempli de un iterador
for i in range (1,11):
    print (i)

my_iterable = range(1,11)
print(my_iterable) #si printamos la variable nos devolvera el range
#pero podemos convertirla en un iterador para manejarlo manualmente
my_iter = iter(range(1,11))
print(my_iter) # si imprmimos nos dira que es un objeto

#cuando esta en ese formato podemos controlar la manera en que se ejecuta
#de forma manual, es decir generar iteraciones manualmente con next()

print(next(my_iter)) #1
print(next(my_iter)) # 2
print(next(my_iter)) #3
print(next(my_iter)) #4

#puedes darle next hasta que ya no tenga mas valores que iterar, de uno en uno 
'''
lo que significa es que no esta generando un rango directamente, si no prograsivamente
lo que hace que el recurso de memoria no sea tan altom dentro de la variable no estan los 
numeros consittuidos en su totalidad, si no mas bien esperando que con cada next que se
realize , lo genere, por eso decimos que es de forma manual
'''
#ten en cuenta hasta que punto vas a iterar debido a que puedes generar un error
#stop iteration


