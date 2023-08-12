datos = [{'Rank': '55', 'CCA3': 'AUS', 'Country/Territory': 'Australia', 'Capital': 'Canberra', 'Continent': 'Oceania', '2022 Population': '26177413', '2020 Population': '25670051', '2015 Population': '23820236', '2010 Population': '22019168', '2000 Population': '19017963', '1990 Population': '17048003', '1980 Population': '14706322', '1970 Population': '12595034', 'Area (km²)': '7692024', 'Density (per km²)': '3.4032', 'Growth Rate': '1.0099', 'World Population Percentage': '0.33'}]

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
resultado = populations_year(datos)
print(resultado)

    