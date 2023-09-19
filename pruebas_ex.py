import random

def verificar_verbo():
    dict_verb = {
        "ir": "go",
        "venir": "come",
        "tomar": "take",
        "dar": "give",
        "mantener": "keep",
        "dejar": "let",
        "ver": "see",
        "decir": "say",
        "parecer": "seem",
        "conseguir": "get",
        "hacer-accion": "do",
        "hacer-crear": "make",
        "poner": "put",
        "ser o estar": "be",
        "enviar": "send",
        "tener": "have"
    }
    
    verbo_aleatorio = random.choice(list(dict_verb.keys()))
    respuesta = input(f"Traduce el verbo '{verbo_aleatorio}': ")
    
    if respuesta.lower() == dict_verb[verbo_aleatorio]:
        print("correcto")
    else:
        print ("incorrecto")

verificar_verbo()
#Esta función seleccionará aleatoriamente un verbo del diccionario dict_verb y te pedirá que lo traduzcas. Si tu respuesta coincide con la traducción correcta, devolverá "Correcto", de lo contrario, devolverá "Incorrecto".
   

