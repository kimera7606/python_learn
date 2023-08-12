#los tipos de variables puedes ser String, booleanos, numerico
#string : o tambien conocidas como cadenas de texto van entre comillas para declararlos
nombre = "Angel"
print(nombre)
apellido = "jimenez"
print(apellido)
#puedes usar tanto comillas simples ('') como comillas dobles ("")
#si quieres resaltar algo con comillas debes usar la comilla diferente a la cual encierras el string
cadena = "ella dice 'hola' "
print (cadena)

full_name = nombre + " " +  apellido
print (full_name)

#booleanos : confirma dos tipos de datos True, False es decir verdero falso
mayor_de_edad = True
print(mayor_de_edad)
soltero = False
print(soltero)
#podemos usar el operador not que niega el estado booleano 
soltero = not soltero
print(soltero)

#numericos: son numeros sean enteros o decimales (float) 
entero = 25
print(entero)
decimal_float = 5.4
print(decimal_float)
#tambien podemos asignarles operaciones matematicas
vidas = 4
lives = 5
union = vidas + lives
print(union)
#tambien podemos hacer operaciones matematicas con variables numericas
union -= 3
print(union)

#Type(variable)  nos ayuda a indicar el tipo de la variable
print(type(nombre))
print(type(mayor_de_edad))
print(type(decimal_float))
print(type(entero))
#input() input nos permite assignar datos a las variables desde la terminal
#pero simepre seran string sin importar el tipo de dato que reciba
nombre = input("what is your name? ")
numero = input("digita un numero ")
print(type(nombre))
print(type(numero))