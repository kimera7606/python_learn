clientes = [
    {
        "nombre" : "angel",
        "apellido" : "jimenez",
        "edad" : "30",
        "ocupacion" : "backend developer"
     },
    
    {
        "nombre" : "carla",
        "apellido" : "reyes",
        "edad" : "51",
        "ocupacion" : "enfermera"
    }
]

def see_list_client ():
    global clientes
    for index, cliente in enumerate(clientes):
        print(f"id: {index} nombre: {cliente['nombre']} {cliente['apellido']} ")
    vacio = print("..." * 30)
    return vacio
    
def add_client():
    nuevo_cliente = {
        "nombre" : input("nombre del cliente a añadir>> : ").lower(),
        "apellido" : input("apellido del cliente a añadir>> : ").lower(),
        "edad" : input("edad del cliente a añadir>> : ").lower(),
        "ocupacion" : input("ocupacion del cliente a añadir>> : ").lower()
    }
    clientes.append(nuevo_cliente)
    print("cliente añadido exitosamente")
    print("..." * 30)

def update_client():
    found = False
    nombre = (input("escribe el nombre del cliente que deseas modificar: >>> "))
    for index, cliente in enumerate(clientes):
        try:
            if nombre == cliente["nombre"] or nombre == cliente["apellido"]:
                found = True
                print (f"id: {index} - nombre: {cliente['nombre']} {cliente['apellido']}")
                print("..." * 30)
        except:
            print("..." * 30)
            return "usuario no encontrado en lista"
        
    if found == True:
        id_client = int(input("digite el id del usuario a modificar: >>> "))
        try:
            clientes[id_client]['nombre'] = input("escribe el nombre: ").lower()
            clientes[id_client]['apellido'] = input("escribe el apellido: ").lower()
            clientes[id_client]['edad'] = input("escribe el edad: ").lower()
            clientes[id_client]['ocupacion'] = input("escribe el ocupacion: ").lower()
            print ("se ha modificado el usuario con exito")
            print("..." * 30)
        except:
            print ("id invalido")
            print("..." * 30)
            
    else :
        print("usuario no existe en lista")
        print("..." * 30)

def delete_client():
    found = False
    nombre = (input("escribe el nombre del cliente que deseas eliminar: >>> "))
    for index, cliente in enumerate(clientes):
        if nombre == cliente["nombre"] or nombre == cliente["apellido"]:
            found = True
            print (f"id: {index} - nombre: {cliente['nombre']} {cliente['apellido']}")
            print("..." * 30)
    if found == True:
        id_client = int(input("digite el id del usuario a eliminar >>> : "))
        try:
            clientes.pop(id_client)
            print("se ha eliminado el cliente con exito")
            print("..." * 30)
        except:
            print("id invalido")
            print("..." * 30)
    else :
        print("usuario no existe en lista")
        print("..." * 30)

def buscar_cliente():
    global clientes
    found = False
    nombre = input("Cual es el nombre del cliente que quieres buscar >> :").lower()
    for index, cliente in enumerate(clientes):
        if nombre == cliente["nombre"] or nombre == cliente["apellido"]:
            found = True
            print(f"id : {index} - nombre : {cliente['nombre']} {cliente['apellido']}")
            print("..." * 30)
    if found == True:
        id_client = int(input("digite el id del usuario para ver mas detalles >>> : "))
        try:
            print(clientes[id_client])
            print("..." * 30)
        except:
            print("id invalido")
            print("..." * 30)
    else :
        print("usuario no existe en lista")
        print("..." * 30)
            

def menu():
    global clientes
    while True:
        menu = int(input("welcome to the customer system \n please, digit same opcion \n 1) * view client list \n 2) * create client \n 3) * search client \n 4) * update client \n 5) * delete client \n >>> : "))
        
        if menu == 1:
            see_list_client()
        elif menu == 2:
            add_client()
        elif menu == 3:
           buscar_cliente()
        elif menu == 4:
            update_client()
        elif menu == 5: 
            delete_client()
        else:
            return "invalid opcion, digit the correct opcion"
if __name__ == "__main__":
    menu()

    


    
    
    
    
