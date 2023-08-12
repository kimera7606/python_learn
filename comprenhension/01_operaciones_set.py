#operaciones entre conjuntos:
#se crean dos conjuntos
conjunto1 = {"colombia", "bolivia", " peru", "guatemala","francia"}
print(conjunto1)
conjunto2 = {"venezuela", "canada", "bolivia", "francia"}
print(conjunto2)
#notese que ambos conjuntos tienen 2 paises repetidos

#union or (|)  : lo que hace es unir ambos conjuntos descartando repetidos
print(("*"*5), "UNION",  ("*" * 5) )
union = conjunto1.union(conjunto2)# une los dos conjuntos sin duplicados
print(union)
union2 = conjunto1 | conjunto2 # se usa el operador | da el mismo resultado
print(union2)
print(("*"*5), "INTERSECTION",  ("*" * 5) )
#interception & : lo que hace es unir los elementos repetidos de ambas listas
intercepcion = conjunto1.intersection(conjunto2)# su resultado sera los elementos comunes
print(intercepcion)
intercepcion2 = conjunto1 & conjunto2 #aqui usamos le operador &
print(intercepcion2)
print(("*"*5), "DIFfERENCE",  ("*" * 5) )
#difference (-)  : deja los elementos del primero conjunto removiendo los del segundo
#es como hacer una resta incluyendo los repetidos de ambos
diferencia = conjunto1.difference(conjunto2)
print(diferencia)
diferencia2 = conjunto1 - conjunto2
print(diferencia2)
print(("*"*5), "SYMETRIC DIFFERENCE",  ("*" * 5) )
#symetric diffeence: hace una union sin los los elementos comunes, lo contrario a intersection
symetric_difference = conjunto1.symmetric_difference(conjunto2)
print (symetric_difference)
symetric_difference2 = conjunto1 ^ conjunto2
print(symetric_difference2)