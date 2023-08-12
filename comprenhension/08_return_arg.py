#return y argumentos
'''
podemos definir parametros con valores por defecto asignando el (= en su parametro)
'''
def find_volume(altura=1, ancho=1, profundidad=2): #asignamos valores por defecto
    return altura * ancho * profundidad, "hola" #con una coma podemos retornar mas
                            # de un valor

result = find_volume() #creamos una variable que contiene el resultado de la funcion
print(result) # como la variable no tiene parametros se usan lo que tiene por defecto

