#while : mientras
#loops son ciclos que repiten alguna accion una y otra vez
#se utiliza la palabra reservada while, se debe crear una condicion para que esta
#no se valla al infinito

counter = 0 #se crea una variable llamada counter
while counter  < 11: #se indica que mientras counter sea menor a 11, el seguira repitiendo su accion
    print(counter)#aqui imprimimos en la terminal el counter
    counter += 1 #aqui le sumamoms a la variable counter 1 , para que se cumpla la condicion de parada del ciclo
#break
#otra manera de parar un loop es creando una condicional que use un break
conteo = 0 # se crea una variable contador
while conteo < 50: #se crea una condicion mientras conteo sea menor a 50 seguira su loop
    print(conteo) #se imprime la variable conteo
    conteo += 1 #se le suma a la variable contador 1 en cada loop
    if conteo == 20: # se crea una condicion en la cual si conteo es igual a 20 
        break #se rompe el loop

print("*" * 25 )
#continue
contador = 0
while contador < 21:
    contador += 1
    if contador < 10: #mientras el contador sea menor a 10
        continue #no se continuara la logica de abajo del continue y seguira en loop solo hasta ahi
    print(contador) 

#tambien se puede decir que continue mientras no se cumpla su condicion va  aobviar 
#toda la logica que tiene debajo, y te regresa el loop hasta su invocacion
    

    