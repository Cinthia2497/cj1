pais = {
    "Chile": 8000,
    "Honduras": 90333,
    "Colombia": 8000000,
    "Guatemala": 130000,
    "Nicaragua": 500000,
    
}

try:
    pais2 = input("Ingrese pais: ")
    print("La poblacion de {} tiene {} habitantes.".format(pais2, format(pais[pais2], ",d")))
except KeyError:
    print("El pais no existe.")