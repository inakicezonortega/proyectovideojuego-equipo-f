
def atacar(atacante , defensor):

    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                 defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "cometa":  # demonio vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "volcanico":  # demonio vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "estelar":  # demonio vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "vacio":  # demonio vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "lunar":  # demonio vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

    elif atacante.tipo == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "cometa":  # cometa vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "volcanico":  # cometa vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "estelar":  # cometa vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "vacio":  # cometa vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "lunar":  # cometa vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

    elif atacante.tipo == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "cometa":  # volcanico vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "estelar":  # volcanico vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "vacio":  # volcanico vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "lunar":  # volcanico vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

    elif atacante.tipo == "estelar":
        if defensor.tipo == "demonio":  # estelar vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "cometa":  # estelar vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "estelar":  # estelar vs  estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "vacio":  # estelar vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "lunar":  # estelar vs  lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

    elif atacante.tipo == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "cometa":  # vacio vs cometa
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

        elif defensor.tipo == "estelar":  # vacio vs estelar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 1.5

        elif defensor.tipo == "vacio":  # vacio vs vacio
            if defensor.HP > defensor.HP_MAX - atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque

        elif defensor.tipo == "lunar":  # vacio vs lunar
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

    elif atacante.tipo == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
            if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
                defensor.HP -= 1
            else:
                defensor.HP_MAX -= atacante.ataque * 0.5

    elif defensor.tipo == "cometa":  # lunar vs cometa
        if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque * 1.5

    elif defensor.tipo == "volcanico":  # lunar vs volcanico
        if defensor.HP > defensor.HP_MAX - atacante.ataque:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque

    elif defensor.tipo == "estelar":  # lunar vs estelar
        if defensor.HP > defensor.HP_MAX - atacante.ataque * 0.5:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque * 0.5

    elif defensor.tipo == "vacio":  # lunar vs vacio
        if defensor.HP > defensor.HP_MAX - atacante.ataque * 1.5:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque * 1.5

    elif defensor.tipo == "lunar":  # lunar vs lunar
        if defensor.HP > defensor.HP_MAX - atacante.ataque:
            defensor.HP -= 1
        else:
            defensor.HP_MAX -= atacante.ataque
