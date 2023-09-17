def empezemos():
    nombre = input("Antes de empezar, primero me gustaira saber tu nombre! escribelo aqui >>> ").upper()
    return print (f"Bienvenid@!! {nombre}")




print ("bievenido a Mundo Aventura!!")
inicio = input("Estas listo o lista para iniciar? (escribe Si para continuar o NO para cancelarla aventua )  >>>").upper()
if inicio == "SI" :
    empezemos()
elif inicio  == "NO" :
    print("awwmm lastima, por un momento pense que entrarias a vivir una buena historia")
else :
    print ("solo debes limitarte a responder si o no")
