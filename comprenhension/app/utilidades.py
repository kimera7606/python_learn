def buscador(data,country):
    resultado = list(filter(lambda x : x["country"] == country, data ))
    if len(resultado) == 0:
        return print("la poblacion de ese pais no se encontro")
    return resultado

