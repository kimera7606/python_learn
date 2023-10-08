dict_verb = {
    "IR": "TO GO",
    "VENIR": "TO COME",
    "TOMAR": "TO TAKE",
    "DAR": "TO GIVE",
    "MANTENER": "TO KEEP",
    "DEJAR": "TO LET",
    "VER": "TO SEE",
    "DECIR": "TO SAY",
    "PARECER": "TO SEEM",
    "CONSEGUIR": "TO GET",
    "HACER-ACCION": "TO DO",
    "HACER-CREAR": "TO MAKE",
    "PONER": "TO PUT",
    "SER O ESTAR": "TO BE",
    "ENVIAR": "TO SEND",
    "TENER": "TO HAVE"
}
def repaso (datos):
    for i in dict_verb:
        print("********************************************")
        prueba = input(f"traduce: {i} >> ").upper()
        if prueba == datos[i]:
            print ("      *** CORRECTO ***")
        else:
            while True:
                print (f" INCORRECTO la esrespuesta es {datos[i]} ")
                prueba = input(f"traduce: {i} >> ").upper()
                if prueba == datos[i]:
                    print ("      *** CORRECTO ***")
                    break
repaso(dict_verb)
            
