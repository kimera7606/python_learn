#metodos de strings
# in() se usa para saber si hay un caracter o string existe en una variable
texto = "ella sabe programar"
print ("sabe" in(texto)) #se escribe primero el caracter seguido del operador que encierra la variable
#la podemos usar en condicionales 
if "Pyton" in texto:
    print ("si existe")
else: 
    print ("no existe!")

#len() da como resultado el numero de datos que tiene un string incluyendo espacios
print(len(texto)) #este operador dara como resultado 19 que sera le numero de letra y espacio

#upper() se utiliza para convertir todo un string a mayuscula
print(texto.upper())
#tambien puede usar en un input al final
texto2 = input("escribe cualquier cosa >> ").upper()
print(texto2) # te devolvera tu msj completamente en mayuscula
#lower() se utiliza para convertir todo un string en minuscula tambien lo puedes usar con inputs
print(texto2.lower())

#count() para contar el numero de apariciones de un caracter
print(texto.count("a")) #mostrara la cantidad de "a" que existen en la variable texto
texto3 = "habia una vez un lobo que comia obejas ese lobo era malo era un lobo muy malo"
print (texto3.count("j")) #mostrara la cantidad de "j" del string
print(texto3.count("malo")) #aqui mostrara las veces que se repite la palabra "malo" en la variable texto3
#swapcase() Se utilia para cambiar invertir mayusculas y minusculas entre si
texto4 = "HOLA COMO  estas tu como va tu proGRAma"
print (texto4.swapcase()) #invertira mayusculas por minusculas y viseverse

#startwith() se utiliza para preguntar si un string comienza con una palabra
print(texto3.startswith("habia")) # el resultado sera True ya que ese string comienza con "habia"
#endswith() se utiliza para pregunrar si un string termina con una palabra
print (texto3.endswith("lobo")) #el resultado sera False, ya que ese strin termina en "malo" no en lobo
#replace() se utiliza para cambiar algun caracter por otro
print(texto3.replace("lobo", "cazador")) #recibe dos parametros el primero es el que se quiere remplezar , y el segundo es el nuevo
#capitaliza () hace que el primer caracter en mayuscula
#title() vuelve los primeros caracteres de las palabras en mayusculas

