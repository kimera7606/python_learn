import utilidades

data = [
    {
        "country" : "venezuela",
        "population" : 300
    },
    {
        "country" : "ecuador",
        "population" : 270
    },
    {
        "country" : "colombia",
        "population" : 511
    },
    {
        "country" : "francia",
        "population" : 895
    },
    {
        "country" : "canada",
        "population" : 842
    },
    {
        "country" : "españa",
        "population" : 163
    },
]
country = input("escribe el pais >>")
resultado = utilidades.buscador(data,country)
print(resultado)