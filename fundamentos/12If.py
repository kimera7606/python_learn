#la condicional if significa SI si esa condicion es verdadera entonces ejecuta el 
#bloque de codigo

numero_misterioso = 10
digita = int(input("digita el numero misterioso >> "))

#aqui la condidicion dice que si el numero que escriba le usuario es igual al numero misterioso
#saldra un msj en caso de no ser asi se ejecutara la otra condicional 
if digita == numero_misterioso:
    print("felicidades adivinaste ")
#else: se utiliza para cuando ninguna de las condiciones de cumple este se ejecutara
else:
    print("sigue intentandolo ")
