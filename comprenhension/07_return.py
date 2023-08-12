#RETURN
'''
normalmente un funcion recibe unos parametros, y deberia retornarme la respuesta
de la funcion para poder usarla en alguna situacion especifica
'''
def suma_enteros(a,b): #creamos un funcion que nos pedira dos parametros
    sum = 0 #creamos una variable suma
    for x in range(a,b): #en un ciclo por x se sumara con sum
        sum += x
    return sum #retornamos para usar el valor de sum en todas sus loops

print(suma_enteros(1,5)) #output 10
print(suma_enteros(1,suma_enteros(1,5))) #output 45
#en este casi de usa la funcion y como parametros se utiliza 1 y la misma funcion
#entra en esa funcion resulve, retorna a la funcion origianl y termina de ejecutarla

#return nos sirve para devolver resultamos valores y datos para luego ser utilizadas
#cuando una fucion no le asignamos un retorno no dara siempre un NONE


