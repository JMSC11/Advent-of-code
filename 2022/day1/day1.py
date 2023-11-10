"""
Se tiene un registro de la cantidad de calorias por comida que tienen los elfos, 
Cada elfo separa su inventario con un espacio en blanco si es que hay un elfo anterior.
Ejemplo:
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

Encuentra al elfo que lleva más calorías. ¿Cuantas calorías lleva?
"""

class Elfo:
    def __init__(self):
        self.comidas = []
        
    def agregar_comida(self, calorias):     
        self.comidas.append(calorias)
        
    def total_calorias(self):      
        return sum(self.comidas)

def encontrar_elfos_con_mas_calorias(elfos, top_rank=3):
    return sorted(elfos, key=lambda elfo: elfo.total_calorias(), reverse=True)[:top_rank]
     
with open("entradas.txt", "r") as file:
    lines = file.read().splitlines()
grupos = []
grupo = []
for line in lines:
    if line:
        grupo.append(int(line))
    else:
        grupos.append(grupo)
        grupo = []
elfos = []
for grupo in grupos:
    elfo = Elfo()
    for calorias in grupo:
        elfo.agregar_comida(calorias)
    elfos.append(elfo)
top_elfos = encontrar_elfos_con_mas_calorias(elfos)
total_calorias_top_elfos = sum([elfo.total_calorias() for elfo in top_elfos])
print(f"Los tres Elfos que llevan más calorías llevan un total de {total_calorias_top_elfos} calorías.")
