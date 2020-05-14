import random

def huir(entrenador):

    x = random.randrange(9)    #Numeros del 0 al 9

    entrenador.lista_equipo["cuerda_huida"] = entrenador.inventario["cuerda_huida"] - 1

    #La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
    if x > -1 and x < 3: return True
    else: return False
