resultados = [ 
    {
    "equipo_local" : "bolivia",
    "equipo_visitante" : "uruguay",
    "anotaciones_local" : 3,
    "anotaciones_visitante" : 1,
    "resultado_local" : "win"
    },
    {
    "equipo_local" : "venezuela",
    "equipo_visitante" : "españa",
    "anotaciones_local" : 5,
    "anotaciones_visitante" : 1,
    "resultado_local" : "win"
    },
    {
    "equipo_local" : "peri",
    "equipo_visitante" : "alemania",
    "anotaciones_local" : 1,
    "anotaciones_visitante" : 6,
    "resultado_local" : "lose"
    },
    {
    "equipo_local" : "francia",
    "equipo_visitante" : "usa",
    "anotaciones_local" : 3,
    "anotaciones_visitante" : 3,
    "resultado_local" : "empate"
    },
    {
    "equipo_local" : "chile",
    "equipo_visitante" : "panama",
    "anotaciones_local" : 0,
    "anotaciones_visitante" : 0,
    "resultado_local" : "empate"
    },
    {
    "equipo_local" : "australia",
    "equipo_visitante" : "italia",
    "anotaciones_local" : 0,
    "anotaciones_visitante" : 2,
    "resultado_local" : "lose"
    },
    {
    "equipo_local" : "russia",
    "equipo_visitante" : "costa rica",
    "anotaciones_local" : 8,
    "anotaciones_visitante" : 7,
    "resultado_local" : "win"
    }
    
]

ganadores = list(filter(lambda x : x["resultado_local"] == "win", resultados))
'''
luego de invocar la lambda como es un diccionario queremos que nos retorne los dict
donde x[] contenga el resultado == "win" y nos retornara esos diccionarios
'''
print(ganadores)