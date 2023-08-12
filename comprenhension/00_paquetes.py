#para importar paquetes que esten en otras carpetas existe una sintaxis
from PQT.moduloUno import funcion_1,funcion_2
'''
primero colocamos FROM luego la carpeta donde estan los modulos y con un punto unir 
el modulo deseado, y luego importamos las funciones que queramos que esten dentro
del paquete
'''
print(funcion_1())
print(funcion_2())

#si estas trabajando en un version anterior a las 3.3 debes crear un archivo __init__.py
#en donde tienes tus paquetes