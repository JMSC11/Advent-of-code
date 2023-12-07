
with open("entradas.txt", "r") as entradas:
    lineas = entradas.read().splitlines()
total = 0
tarjetas_obtenidas = {

}
for i, linea in enumerate(lineas, start = 1):
    partes = linea.split(':')[1].strip().split('|')
    set1 = set(map(int, partes[0].strip().split()))
    set2 = set(map(int, partes[1].strip().split()))
    print(f"primer for: {i}")
    # numeros_ganadores = len(set1.intersection(set2))
    # if numeros_ganadores > 0:
    #     potencia = numeros_ganadores -1
    #     total += 2**potencia
    tarjetas = len(set1.intersection(set2))
    fin_rango = i + tarjetas +1
    #print(tarjetas)
    for num in range(i,fin_rango):
        if num in tarjetas_obtenidas:
            for j in range(1, tarjetas_obtenidas[num] +1):
                print(f'{j} copia de {tarjetas_obtenidas[i]}')
                tarjetas_obtenidas[num] += 1
        else:
            tarjetas_obtenidas[num] = 1


        print(tarjetas_obtenidas)


    


    