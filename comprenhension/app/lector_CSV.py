import csv #importamos el modulo csv que puede leer este tipo de archivos

def lector_csv(ruta): #creamos una funcion con parametro de ruta del archivo a leer
    with open(ruta) as archivo_csv: #abrimos el documento
        lector = csv.reader(archivo_csv, delimiter=",") #creamos un lector con el modulo
        indice = next(lector) #con next ya que es iterable creamos el indice
        data = [] #una variable lista vacia que recibira los datos
        for i in lector: #este ciclo for entrara en el resto del documento
            union = zip(indice,i) #usamos zip para unir el indice y el resot de los datos
            dict_paises = {dato : pais for dato,pais in union} #creamos un diccionario
            data.append(dict_paises)#enviamos cada diccionario a la lista vacia
        return data #retornamos la lista que ahora contiene diccionarios
        
if __name__ == "__main__":
    data = lector_csv("app/data.csv") #usamos la funcion y le agregamos la ruta del csv
    print(data[0]) # buscamos el primer dato para corroborar que todo este correcto
    
