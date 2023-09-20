from random import choice
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

dict_pronombres = {
    "YO" :"I",
    "TU" : "YOU",
    "NOSOTROS" : "WE",
    "ELLA" : "SHE",
    "EL" : "HE",
    "ESO" : "IT",
    "ELLOS" : "THEY",
    "USTEDES" : "YOU",
    
}

frase_pronombre_and_verbs = {
    "YO VOY" : "I GO",
    "TU VAS" : "YOU GO",
    "NOSOTROS VAMOS" : "WE GO",
    "EL VA" : "HE GOES",
    "ELLA VA" : "SHE GOES",
    "ESO VA" : "IT GOES",
    "ELLOS VAN" : "THEY GO",
    "USTEDES VAN" : "YOU GO",
    "YO VENGO" : "I COME",
    "TU VIENES" : "YOU COME",
    "NOSOTROS VENIMOS" : "WE COME",
    "EL VIENE" : "HE COMES",
    "ELLA VIENE" : "SHE COMES",
    "ESO VIENE" : "IT COMES",
    "ELLOS VIENEN" : "THEY COME",
    "USTEDES VIENEN" : "YOU COME",
    "YO DOY" : "I GIVE",
    "TU DAS" : "YOU GIVE",
    "NOSOTROS DAMOS" : "WE GIVE",
    "EL DA" : "HE GIVES",
    "ELLA DA" : "SHE GIVES",
    "ESO DA" : "IT GIVES",
    "ELLOS DAN" : "THEY GIVE",
    "USTEDES DAN" : "YOU GIVE",
    "YO TOMO" : "I TAKE",
    "TU TOMAS" : "YOU TAKE",
    "NOSOTROS TOMAMOS" : "WE TAKE",
    "EL TOMA" : "HE TAKES",
    "ELLA TOMA" : "SHE TAKES",
    "ESO TOMA" : "IT TAKES",
    "ELLOS TOMAN" : "THEY TAKE",
    "USTEDES TOMAN" : "YOU TAKE",
    "YO MANTENGO" : "I KEEP",
    "TU MANTIENES" : "YOU KEEP",
    "NOSOTROS MANTENEMOS" : "WE KEEP",
    "EL MANTIENE" : "HE KEEPS",
    "ELLA MANTIENE" : "SHE KEEPS",
    "ESO MANTIENE" : "IT KEEPS",
    "ELLOS MANTIENEN" : "THEY KEEP",
    "USTEDES MANTIENEN" : "YOU KEEP",
    "YO DEJO" : "I LET",
    "TU DEJAS" : "YOU LET",
    "NOSOTROS DEJAMOS" : "WE LET",
    "EL DEJA" : "HE LETS",
    "ELLA DEJA" : "SHE LETS",
    "ESO DEJA" : "IT LETS",
    "ELLOS DEJAN" : "THEY LET",
    "USTEDES DEJAN" : "YOU LET",
    "YO VEO" : "I SEE",
    "TU VES" : "YOU SEE",
    "NOSOTROS VEMOS" : "WE SEE",
    "EL VE" : "HE SEES",
    "ELLA VE" : "SHE SEES",
    "ESO VE" : "IT SEES",
    "ELLOS VEN" : "THEY SEE",
    "USTEDES VEN" : "YOU SEE",
    "YO PAREZCO" : "I SEEM",
    "TU PARECES" : "YOU SEEM",
    "NOSOTROS PARECEMOS" : "WE SEEM",
    "EL PARECE" : "HE SEEMS",
    "ELLA PARECE" : "SHE SEEMS",
    "ESO PARECE" : "IT SEEMS",
    "ELLOS PARECEN" : "THEY SEEM",
    "USTEDES PARECEN" : "YOU SEEM",
    "YO CONSIGO" : "I GET",
    "TU CONSIGUES" : "YOU GET",
    "NOSOTROS CONSEGUIMOS" : "WE GET",
    "EL CONSIGUE" : "HE GETS",
    "ELLA CONSIGUE" : "SHE GETS",
    "ESO CONSIGUE" : "IT GETS",
    "ELLOS CONSIGUEN" : "THEY GET",
    "USTEDES CONSIGUEN" : "YOU GET",
    "YO HAGO/ACCION" : "I DO",
    "TU HACES/ACCION" : "YOU DO",
    "NOSOTROS HACEMOS/ACCION" : "WE DO",
    "EL HACE/ACCION" : "HE DOES",
    "ELLA HACE/ACCION" : "SHE DOES",
    "ESO HACE/ACCION" : "IT DOES",
    "ELLOS HACE/ACCION" : "THEY DO",
    "USTEDES HACEN/ACCION" : "YOU DO",
    "YO HAGO/CREAR" : "I MAKE",
    "TU HAGO/CREAR" : "YOU MAKE",
    "NOSOTROS HACEMOS/CREAR" : "WE MAKE",
    "EL HACE/CREAR" : "HE MAKES",
    "ELLA HACE/CREAR" : "SHE MAKES",
    "ESO HACE/CREAR" : "IT MAKES",
    "ELLOS HACEN/CREAR" : "THEY MAKES",
    "USTEDES HACEN/CREAR" : "YOU MAKE",
    "YO PONGO" : "I PUT",
    "TU PONES" : "YOU PUT",
    "NOSOTROS PONEMOS" : "WE PUT",
    "EL PONE" : "HE PUTS",
    "ELLA PONE" : "SHE PUTS",
    "ESO PONE" : "IT PUTS",
    "ELLOS PONEN" : "THEY PUT",
    "USTEDES PONEN" : "YOU PUT",
    "YO SOY/ESTOY" : "I AM",
    "TU ERES/ESTAS" : "YOU ARE",
    "NOSOTROS SOMOS/ESTAMOS" : "WE ARE",
    "EL ES/ESTA" : "HE IS",
    "ELLA ES/ESTA" : "SHE IS",
    "ESO ES/ESTA" : "IT IS",
    "ELLOS SON/ESTAN" : "THEY ARE",
    "USTEDES SON/ESTAN" : "YOU ARE",
    "YO ENVIE" : "I SEND",
    "TU ENVIAS" : "YOU SEND",
    "NOSOTROS ENVIAMOS" : "WE SEND",
    "EL ENVIA" : "HE SENDS",
    "ELLA ENVIA" : "SHE SENDS",
    "ESO ENVIA" : "IT SENDS",
    "ELLOS ENVIAN" : "THEY SEND",
    "USTEDES ENVIAN" : "YOU SEND",
    "YO TENGO" : "I HAVE",
    "TU TIENES" : "YOU HAVE",
    "NOSOTROS TENEMOS" : "WE HAVE",
    "EL TIENE" : "HE HAS",
    "ELLA TIENE" : "SHE HAS",
    "ESO TIENE" : "IT HAS",
    "ELLOS TIENEN" : "THEY HAVE",
    "USTEDES TIENEN" : "YOU HAVE",  
}

tiempos_will = {
    "YO IRE" : "I WILL GO",
    "TU IRAS" : "YOU WILL GO",
    "NOSOTROS IREMOS" : "WE WILL GO",
    "EL IRA" : "HE WILL GOES",
    "ELLA IRA" : "SHE WILL GOE",
    "ESO IRA" : "IT WILL GOE",
    "ELLOS IRAN" : "THEY WILL GO",
    "USTEDES IRAN" : "YOU WILL GO",
    "YO VENDRE" : "I WILL COME",
    "TU VENDRAS" : "YOU WILL COME",
    "NOSOTROS VENDREMOS" : "WE WILL COME",
    "EL VENDRA" : "HE WILL COME",
    "ELLA VENDRA" : "SHE WILL COME",
    "ESO VENDRA" : "IT WILL COME",
    "ELLOS VENDRAN" : "THEY WILL COME",
    "USTEDES VENDRAN" : "YOU WILL COME",
    "YO DARE" : "I WILL GIVE",
    "TU DARAS" : "YOU WILL GIVE",
    "NOSOTROS DAREMOS" : "WE WILL GIVE",
    "EL DARA" : "HE WILL GIVE",
    "ELLA DARA" : "SHE WILL GIVE",
    "ESO DARA" : "IT WILL GIVE",
    "ELLOS DRAN" : "THEY WILL GIVE",
    "USTEDES DARAN" : "YOU WILL GIVE",
    "YO TOMARE" : "I WILL TAKE",
    "TU TOMARAS" : "YOU WILL TAKE",
    "NOSOTROS TOMAREMOS" : "WE WILL TAKE",
    "EL TOMARA" : "HE WILL TAKE",
    "ELLA TOMARA" : "SHE WILL TAKE",
    "ESO TOMARA" : "IT WILL TAKE",
    "ELLOS TOMARAN" : "THEY WILL TAKE",
    "USTEDES TOMARAN" : "YOU WILL TAKE",
    "YO MANTENDRE" : "I WILL KEEP",
    "TU MANTENDRA" : "YOU WILL KEEP",
    "NOSOTROS MANTENDREMOS" : "WE WILL KEEP",
    "EL MANTENDRA" : "HE WILL KEEP",
    "ELLA MANTENDRA" : "SHE WILL KEEP",
    "ESO MANTENDRA" : "IT WILL KEEP",
    "ELLOS MANTENDRAN" : "THEY WILL KEEP",
    "USTEDES MANTENDRAN" : "YOU WILL KEEP",
    "YO DEJARE" : "I WILL LET",
    "TU DEJARAS" : "YOU WILL LET",
    "NOSOTROS DEJAREMOS" : "WE WILL LET",
    "EL DEJARA" : "HE WILL LET",
    "ELLA DEJARA" : "SHE WILL LET",
    "ESO DEJARA" : "IT WILL LET",
    "ELLOS DEJARAN" : "THEY WILL LET",
    "USTEDES DEJARAN" : "YOU WILL LET",
    "YO VERE" : "I WILL SEE",
    "TU VERAS" : "YOU WILL SEE",
    "NOSOTROS VEREMOS" : "WE WILL SEE",
    "EL VERA" : "HE WILL SEE",
    "ELLA VERA" : "SHE WILL SEE",
    "ESO VERA" : "IT WILL SEE",
    "ELLOS VERAN" : "THEY WILL SEE",
    "USTEDES VERAN" : "YOU WILL SEE",
    "YO PAREZCERE" : "I WILL SEEM",
    "TU PARECERAS" : "YOU WILL SEEM",
    "NOSOTROS PARECEREMOS" : "WE WILL SEEM",
    "EL PARECERA" : "HE WILL SEEM",
    "ELLA PARECERA" : "SHE WILL SEEM",
    "ESO PARECERA" : "IT WILL SEEM",
    "ELLOS PARECERAN" : "THEY WILL SEEM",
    "USTEDES PARECERAN" : "YOU WILL SEEM",
    "YO CONSEGUIRE" : "I WILL GET",
    "TU CONSEGUIRAS" : "YOU WILL GET",
    "NOSOTROS CONSEGUIREMOS" : "WE WILL GET",
    "EL CONSIGUIRA" : "HE WILL GET",
    "ELLA CONSIGUIRA" : "SHE WILL GET",
    "ESO CONSIGUIRA" : "IT WILL GET",
    "ELLOS CONSIGUIRAN" : "THEY WILL GET",
    "USTEDES CONSIGUIRAN" : "YOU WILL GET",
    "YO HARE/ACCION" : "I WILL DO",
    "TU HARAS/ACCION" : "YOU WILL DO",
    "NOSOTROS HAREMOS/ACCION" : "WE WILL DO",
    "EL HARA/ACCION" : "HE WILL DO",
    "ELLA HARA/ACCION" : "SHE WILL DO",
    "ESO HARA/ACCION" : "IT WILL DO",
    "ELLOS HARAN/ACCION" : "THEY WILL DO",
    "USTEDES HARAN/ACCION" : "YOU WILL DO",
    "YO HARE/CREAR" : "I WILL MAKE",
    "TU HARAS/CREAR" : "YOU WILL MAKE",
    "NOSOTROS HAREMOS/CREAR" : "WE WILL MAKE",
    "EL HARA/CREAR" : "HE WILL MAKE",
    "ELLA HARA/CREAR" : "SHE WILL MAKE",
    "ESO HARA/CREAR" : "IT WILL MAKE",
    "ELLOS HARAN/CREAR" : "THEY WILL MAKE",
    "USTEDES HARAN/CREAR" : "YOU WILL MAKE",
    "YO PONDRE" : "I WILL PUT",
    "TU PONDRAS" : "YOU WILL PUT",
    "NOSOTROS PONDREMOS" : "WE WILL PUT",
    "EL PONDRA" : "HE WILL PUT",
    "ELLA PONDRA" : "SHE WILL PUT",
    "ESO PONDRA" : "IT WILL PUT",
    "ELLOS PONDRAN" : "THEY WILL PUT",
    "USTEDES PONDRAN" : "YOU WILL PUT",
    "YO SERE/ESTARE" : "I WILL AM",
    "TU SERAS/ESTARAS" : "YOU WILL ARE",
    "NOSOTROS SEREMOS/ESTAREMOS" : "WE WILL ARE",
    "EL SERA/ESTARA" : "HE WILL BE",
    "ELLA SERA/ESTARA" : "SHE WILL BE",
    "ESO SERA/ESTARA" : "IT WILL BE",
    "ELLOS SERAN/ESTARAN" : "THEY WILL ARE",
    "USTEDES SORAN/ESTARAN" : "YOU WILL ARE",
    "YO ENVIARE" : "I WILL SEND",
    "TU ENVIARAS" : "YOU WILL SEND",
    "NOSOTROS ENVIAREMOS" : "WE WILL SEND",
    "EL ENVIARA" : "HE WILL SEND",
    "ELLA ENVIARA" : "SHE WILL SEND",
    "ESO ENVIARA" : "IT WILL SEND",
    "ELLOS ENVIRAN" : "THEY WILL SEND",
    "USTEDES ENVIRAN" : "YOU WILL SEND",
    "YO TENDRE" : "I WILL HAVE",
    "TU TENDRAS" : "YOU WILL HAVE",
    "NOSOTROS TENDREMOS" : "WE WILL HAVE",
    "EL TENDRA" : "HE WILL HAVE",
    "ELLA TENDRA" : "SHE WILL HAVE",
    "ESO TENDRA" : "IT WILL HAVE",
    "ELLOS TENDRAN" : "THEY WILL HAVE",
    "USTEDES TENDRAN" : "YOU WILL HAVE",  
}

def pracitca_dict(data):
    aciertos = 0
    fallos = 0
    print('''
          veras a continuacion una serie de verbos en español, tu tarea es escribirlos al ingles.
          (en caso de que quieras salir de la practica escribe EXIT)
          ''')
    while True:
        print(".....................................................")
        print(f"*aciertos* : {aciertos}, *fallos* : {fallos}")
        verb_random = choice(list(data.keys()))
        respuesta = input(f"traduce al ingles *  '{verb_random}' * >>> ").upper()
        if respuesta == "EXIT" :
            break
        elif data[verb_random] == respuesta:
            print ("                 *correcto*                ")
            aciertos += 1
        else :
            print(f"    *incorrecto*       la respuesta era {data[verb_random]}" )
            fallos +=1


def verbos_pasado():
    pass
while True:
    def start():
        print("bienvenido a : practicas de ingles")
        print('''
            1) verbos importantes
            2) pronombres
            3) pronombres + verbos 
            4) tiempos futuro will 
            5) tiempos would, may, migth
            6) verbos importantes en pasado (pronto)
            ''')
        elije = int(input("digita la opcion de la cual quieres aprender >>> "))

        if elije == 1 :
            pracitca_dict(dict_verb)
        elif elije == 2 : 
            pracitca_dict(dict_pronombres)
        elif elije == 3 :
            pracitca_dict (frase_pronombre_and_verbs)
        elif elije == 4:
            pracitca_dict(tiempos_will)
        elif elije == 5 :
            verbos_pasado()

    if __name__ == "__main__":
        start()