#and 
'''
para que sea True ambas condiciones deben ser True
si alguna de las condiciones es falsa, dara false
'''

print (True and True)
print (False and False)
print (True and False)

#tambien lo podemos usar con operadores de comparacion ejemplo

print (5 > 4 and 3 > 2)
print (10 > 11 and 41 < 50)

#un ejemplo de como pùede usarse
stock = int(input("ingrese numero del stock >> "))
print (stock >= 100 and stock <= 100)
#mientras el numero ingresado sea mayor a 100 y menor  a 1000 sera True

#or
#este operador da como resultado True siempre y cuando minimo una de las condiciones sea True
#para que de falso ambas condiciones deben ser falsas

print (True or True)
print (False or False)
print (True or False)

#ejemplo de como podemos usarlo
role = input("elije un rol >>")
print (role == "admin" or role == "gerente")

