from random import randint
paises = ["usa", "venezuela", "canada", "francia"]
population = {i : randint(100,1000) for i in paises}

#solo dara los valores que sean mayor a 500
result = {clave:valor for (clave, valor) in population.items() if valor > 500 }
print(result)

texto = "hola como estas"
unique = {l : l.upper() for l in texto if l in "aeiou"}
'''
creamos clave y el valro sera la clave pero en mayuscula, e iteramos dentro del texto
con la ocndificon de que se agregaran solo cuando i este dentro de las vocales
'''
print(unique)

