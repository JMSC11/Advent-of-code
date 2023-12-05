def getCantidadMinima(cantidad, color, cantidad_minima):
    if cantidad >= cantidad_minima[color]:
        cantidad_minima[color] = cantidad
    #print(f'El diccionario es:{cantidad_minima}')
    return cantidad_minima

with open('entradas.txt', 'r') as entradas:
    games = entradas.read().splitlines()

cubes = ["red", "blue", "green"]
bolsa = {
    'red': 12,
    'green': 13,
    'blue': 14
}

suma_ids = 0
suma_potencias = 0
for j, game in enumerate(games, start=1):  # j es el id del juego
    cantidad_minima = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    _, conjuntos = game.split(": ")
    conjuntos = conjuntos.split("; ")
    es_posible = True  
    for conjunto in conjuntos:
        partes = conjunto.split(", ")
        for parte in partes:
            cantidad, color = parte.split(" ", 1)
            cantidad = int(cantidad)
            cantidad_minima = getCantidadMinima(cantidad, color, cantidad_minima)
            if cantidad > bolsa[color]:
                es_posible = False
                #break   --parte1 --

        #if not es_posible:  --parte1--
            #break           --parte1--  
    suma_potencias += cantidad_minima["red"] * cantidad_minima["blue"] * cantidad_minima["green"]
    print(f'La cantidad minima es: {cantidad_minima}')
    print("------------------------")
    if es_posible:
        suma_ids += j 

print(f'Suma total de IDs de juegos posibles: {suma_ids}') #Parte1
print(f'La suma de las potencias es: {suma_potencias}') #Parte2