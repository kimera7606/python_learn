import csv

def lector_csv(ruta):
    with open(ruta,"r") as archivo_csv:
        lector = csv.reader(archivo_csv, delimiter=",")
        indice = next(lector)
        data = []
        for i in lector:
            union = zip(indice,i)
            dict_paises = {dato :pais for dato, pais in union}
            data.append(dict_paises)
        return data

def buscador_paises(datos,pais):
    result = list(filter(lambda datos : datos["Country/Territory"] == pais,datos ))
    return result

def populations_year(data):
    keys = ["population 2022", "population 2020", "2015 Population",
            "2010 Population", "2000 Population","1990 Population",
            "1980 Population","1970 Population"]
    values = []
    for i in data:
        values.append(i["2022 Population"])
        values.append(i["2020 Population"])
        values.append(i["2015 Population"])
        values.append(i["2010 Population"])
        values.append(i["2000 Population"])
        values.append(i["1990 Population"])
        values.append(i["1980 Population"])
        values.append(i["1970 Population"])

    union = zip(keys,values)
    dict_result = { k : v for k,v in union}
    return dict_result

if __name__ == "__main__":
    
    resultado = lector_csv("app/data.csv")

    buscar = input("Escribe un pais >> ").title()
    busqueda =buscador_paises(resultado,buscar)
    poblacion =populations_year(busqueda)
    print(poblacion)
