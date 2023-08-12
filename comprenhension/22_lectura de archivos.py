#como leeer un archivo txt desde python
#primero tenemos que usar un operador llamado open()
file = open("./texto.txt") #en este caso la asignamos a una variable
#open () lleva como parametros la ubicacion o el path del documento a leer
print (file.read()) #podmeos leerlo con un print y a la variable usamos 
#el operador read() que es leer, una vez esto se vera impreso en la terminal

file2 = open("./texto.txt")
print (file2.read())

'''
lo que hicimos con le metodo read es tomar todo el texto y leerlo directamente
pero tambien podemos leerlo linea por linea con readline, para qeu este lea linea por linea
muy parecido a next () de los iterables
'''
fiel3 = open("./texto.txt")
print(fiel3.readline())
file.close()
file2.close()
fiel3.close()
#luego de abrir los documentos debemos cerrarlos eso lo hacmeos con file.close()

#la forma mas comun de leer y abrir archivos en python es con with ya que este cierra
#automaticamente
with open("./texto.txt") as file: #importante: podemos ver que el as , es un alias
    for line in file: # al archivo se le asigna un alias
        print(line)#siquisieramos añador texto en el archivo lo hare con el operador whrite y en el 
#open() agregar el "r+" que nos permite escirbir y leer

with open("./texto.txt", "r+") as texto: # en el open agragar el "r+"
    
    texto.write("\n Que te hecho de menos, que mi mundo es pequeño, si me dejas de amar")
    #usamos el alias del documento mas el operador whrite("") donde agregamos mas texto
    for i in texto: #con un ciclo for imprimimos el texto con la nueva modificacion
        print(i)
#para sobrescribir todo el contenido, se utiliza "w+" pero este borra el contenido para
#sobrescribir uno nuevo asi que cuidado_! 

