usuarios = [{}]
def salida(numero):
    if numero == 3:
        print("Gracias por preferirnos , hasta pronto")
        exit()

def ingreso(numero):
    global usuarios
    if numero == 1:
        concordancia = {}
        id = input("por favor escriba su asuario >> ")
        contraseña = input("ingrese su contraseña >> ")
        concordancia[id] = contraseña
        error = {}
        for i in usuarios:
            if concordancia == i:
                print("bienvenido al sistema")
            elif error == i:
                print(" ")
            else:
                print("usuario no registrado en sistema")
                
        

def nuevo_ingreso(numero):
    global usuarios
    if numero == 2:
        id = input("por favor escriba su usuario >> ")
        contraseña = input("ingrese su contraseña >> ")
        usuarios.append({id:contraseña})
        print("usuario Creado satisfactoriamente")

if __name__ == "__main__":
            
    while True:
        opciones =int(input('''
                ***bienvenidos al sistema***
            Elija una opcion para continuar:
        1) Ingreso al sistema
        2) Registro nuevo usuario
        3) Salir
        >>> '''))
        salida(opciones)
        nuevo_ingreso(opciones)
        ingreso(opciones)
