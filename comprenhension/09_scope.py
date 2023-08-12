#escope o alcanze:
'''
se refiere cuando creamos un variable o funcion y que alcanze tiene en el codigo
para poder referenciarnos, usar, o trabajar con ellas
'''
price = 100 # se crea una variable, esta tiene un alzanze y podemos usarla
print(price) # se imprime la variable, y funciona en este archivo que esta dentro de el
def impresion (): #definimos una funcion
    return print(price *2) #esta funcion usa el scope de price y lo imprime
impresion() #output 200

def incremento ():
    price = 400 # esta variable pertenece a la funcion solo puede usarse dentro
    resultado = price * 2 #la variable price de aqui no tiene que ver con la de afuera
    return resultado

print(incremento())

try:
    print(resultado) # tratar de imprmir una variable que esta dentro de una funcion
#arrojara error de scope ya que solo puede ser usada y vivir en la funcion no fuera
except:
    print("error , trataste de imprimir una variable local de funcion")



