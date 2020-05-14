

def combate():

    elegirPokemon()     #Elegir Pokemon para combatir

    while True:

        ataqueEnemigo() #Daña Pokemon aliado

        if HP != 0:     #Si el Pokemon aliado esta vivo

            turnoAliado()  # Llamada a la funcion turno Aliado

            ataqueAliado()  # Daña Pokemon enemigo

        else:           #Si el Pokemon aliado muere

            elegirPokemon()

            turnoAliado()

        if HP_enemigo == 0: #Comprobar si el enemigo ha muerto
            repartir_exp()
            break

        else: continue



def turnoAliado():

    while True:
        respuesta = int(input("Elige una respuesta: atacar(1), objeto(2), cambiar Pokemon(3)"))

        if respuesta == 1: break

        if respuesta == 2:
            usarObjeto()
            break

        if respuesta == 3:
            elegirPokemon()

        else:
            print("Elige una respuesta valida")
