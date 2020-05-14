def turno_aliado(entrenador,rival,accion):

    pokemon_aliado = entrenador.lista_equipo[0]
    pokemon_enemigo = rival.lista_equipo[0]

    while True:
        if accion == 1:
            pokemon_enemigo.HP = atacar(pokemon_aliado.tipo,pokemon_enemigo.tipo,pokemon_enemigo.HP,pokemon_enemigo.HP_MAX,pokemon_aliado.ataque)
        elif accion == 2:
            pocion(entrenador,pokemon_aliado.HP,pokemon_aliado.HP_MAX)
        elif accion == 3:
        elif accion == 4:
        else: print("Error")









def pocion(entrenador, vida_aliado, vida_maxima):
    if vida_aliado != vida_maxima and entrenador["pocion"]!=0:
        entrenador.inventario.pop("pocion")
        return (vida_aliado * 1.5)

    else: return vida_maxima

def atacar(tipo_aliado , tipo_enemigo,hp_enemigo,hp_total,ataque):
    if tipo_aliado == "demonio":
        if tipo_enemigo == "demonio":  # demonio vs demonio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "cometa":  # demonio vs cometa
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "volcanico":  # demonio vs volcanico
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "estelar":  # demonio vs estelar
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "vacio":  # demonio vs vacio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "lunar":  # demonio vs lunar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

    elif tipo_aliado == "cometa":
        if tipo_enemigo == "demonio":  # cometa vs demonio
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "cometa":  # cometa vs cometa
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "volcanico":  # cometa vs volcanico
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "estelar":  # cometa vs estelar
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "vacio":  # cometa vs vacio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "lunar":  # cometa vs lunar
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

    elif tipo_aliado == "volcanico":
        if tipo_enemigo == "demonio":  # volcanico vs demonio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "cometa":  # volcanico vs cometa
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "volcanico":  # volcanico vs volcanico
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "estelar":  # volcanico vs estelar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "vacio":  # volcanico vs vacio
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "lunar":  # volcanico vs lunar
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

    elif tipo_aliado == "estelar":
        if tipo_enemigo == "demonio":  # estelar vs demonio
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "cometa":  # estelar vs cometa
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "volcanico":  # estelar vs volcanico
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "estelar":  # estelar vs  estelar
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "vacio":  # estelar vs vacio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "lunar":  # estelar vs  lunar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

    elif tipo_aliado == "vacio":
        if tipo_enemigo == "demonio":  # vacio vs demonio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "cometa":  # vacio vs cometa
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "volcanico":  # vacio vs volcanico
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

        elif tipo_enemigo == "estelar":  # vacio vs estelar
            if hp_enemigo > hp_total - ataque * 1.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 1.5

        elif tipo_enemigo == "vacio":  # vacio vs vacio
            if hp_enemigo > hp_total - ataque:
                return hp_enemigo - 1
            else:
                return hp_total - ataque

        elif tipo_enemigo == "lunar":  # vacio vs lunar
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

    elif tipo_aliado == "lunar":
        if tipo_enemigo == "demonio":  # lunar vs demonio
            if hp_enemigo > hp_total - ataque * 0.5:
                return hp_enemigo - 1
            else:
                return hp_total - ataque * 0.5

    elif tipo_enemigo == "cometa":  # lunar vs cometa
        if hp_enemigo > hp_total - ataque * 1.5:
            return hp_enemigo - 1
        else:
            return hp_total - ataque * 1.5

    elif tipo_enemigo == "volcanico":  # lunar vs volcanico
        if hp_enemigo > hp_total - ataque:
            return hp_enemigo - 1
        else:
            return hp_total - ataque

    elif tipo_enemigo == "estelar":  # lunar vs estelar
        if hp_enemigo > hp_total - ataque * 0.5:
            return hp_enemigo - 1
        else:
            return hp_total - ataque * 0.5

    elif tipo_enemigo == "vacio":  # lunar vs vacio
        if hp_enemigo > hp_total - ataque * 1.5:
            return hp_enemigo - 1
        else:
            return hp_total - ataque * 1.5

    elif tipo_enemigo == "lunar":  # lunar vs lunar
        if hp_enemigo > hp_total - ataque:
            return hp_enemigo - 1
        else:
            return hp_total - ataque