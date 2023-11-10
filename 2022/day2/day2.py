"""
Códigos encriptados oponente:
    A: Piedra
    B: Papel
    C: Tijeras
Códigos encriptados propios:
    X: Piedra
    Y: Papel
    Z: Tijeras
Puntuaciones:
    Triunfo: 6
    Empate: 3
    Derrota: 0

    Piedra: 1
    Papel: 2
    Tijeras: 3

"""

#Observar que cada opción tiene un valor, por lo tanto:
class Juego:
    puntajes = {
        'X': 1, 
        'Y': 2,
        'Z': 3,
        'triunfo': 6,
        'empate': 3,
        'derrota': 0
    }

    def __init__(self):
        self.score_total = 0

    def calcular_score(self, opcion_propia, resultado):
        return self.puntajes[opcion_propia] + self.puntajes[resultado]

    def partida(self, opcion_oponente, opcion_propia):
        if opcion_oponente == 'A': #piedra
            if opcion_propia == 'X':
                score_ronda = self.calcular_score(opcion_propia, 'empate')
            if opcion_propia == 'Y':
                score_ronda = self.calcular_score(opcion_propia, 'triunfo')
            if opcion_propia == 'Z':
                score_ronda = self.calcular_score(opcion_propia, 'derrota')
        elif opcion_oponente == 'B':#papel
            if opcion_propia == 'X':
                score_ronda = self.calcular_score(opcion_propia, 'derrota')
            if opcion_propia == 'Y':
                score_ronda = self.calcular_score(opcion_propia, 'empate')
            if opcion_propia == 'Z':
                score_ronda = self.calcular_score(opcion_propia, 'triunfo')
        elif opcion_oponente == 'C':#tijera
            if opcion_propia == 'X':
                score_ronda = self.calcular_score(opcion_propia, 'triunfo')
            if opcion_propia == 'Y':
                score_ronda = self.calcular_score(opcion_propia, 'derrota')
            if opcion_propia == 'Z':
                score_ronda = self.calcular_score(opcion_propia, 'empate')
        self.score_total += score_ronda

    def partida_segunda_parte(self, opcion_oponente, opcion_propia):
        """
        opcion propia
            X = lose
            Y = draw
            Z = win
        """
        opcion_requerida = {
            'piedra': 'X',
            'papel': 'Y',
            'tijera': 'Z',
        }
        if opcion_oponente == 'A': #piedra
            if opcion_propia == 'X':
                score_ronda = self.calcular_score(opcion_requerida['tijera'], 'derrota')
            if opcion_propia == 'Y':
                score_ronda = self.calcular_score(opcion_requerida['piedra'], 'empate')
            if opcion_propia == 'Z':
                score_ronda = self.calcular_score(opcion_requerida['papel'], 'triunfo')
        elif opcion_oponente == 'B':#papel
            if opcion_propia == 'X':
                score_ronda = self.calcular_score(opcion_requerida['piedra'], 'derrota')
            if opcion_propia == 'Y':
                score_ronda = self.calcular_score(opcion_requerida['papel'], 'empate')
            if opcion_propia == 'Z':
                score_ronda = self.calcular_score(opcion_requerida['tijera'], 'triunfo')
        elif opcion_oponente == 'C':#tijera
            if opcion_propia == 'X':
                score_ronda = self.calcular_score(opcion_requerida['papel'], 'derrota')
            if opcion_propia == 'Y':
                score_ronda = self.calcular_score(opcion_requerida['tijera'], 'empate')
            if opcion_propia == 'Z':
                score_ronda = self.calcular_score(opcion_requerida['piedra'], 'triunfo')
        
        
        self.score_total += score_ronda


juego = Juego()

with open('entradas.txt', 'r') as file:
    for line in file:
        opcion_oponente, opcion_propia = line.strip().split()
        juego.partida(opcion_oponente, opcion_propia)
        #juego.partida_segunda_parte(opcion_oponente, opcion_propia)

print(f'Score Total: {juego.score_total}')




