
def atacar(atacante , defensor):
    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "cometa":  # demonio vs cometa
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "volcanico":  # demonio vs volcanico

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "estelar":  # demonio vs estelar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "vacio":  # demonio vs vacio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "lunar":  # demonio vs lunar

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

    elif atacante.tipo == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "cometa":  # cometa vs cometa
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "volcanico":  # cometa vs volcanico

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "estelar":  # cometa vs estelar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "vacio":  # cometa vs vacio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "lunar":  # cometa vs lunar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

    elif atacante.tipo == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "cometa":  # volcanico vs cometa
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "estelar":  # volcanico vs estelar

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "vacio":  # volcanico vs vacio

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "lunar":  # volcanico vs lunar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

    elif atacante.tipo == "estelar":
        if defensor.tipo == "demonio":  # estelar vs demonio

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "cometa":  # estelar vs cometa
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "estelar":  # estelar vs  estelar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "vacio":  # estelar vs vacio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "lunar":  # estelar vs  lunar

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

    elif atacante.tipo == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "cometa":  # vacio vs cometa

                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "estelar":  # vacio vs estelar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "vacio":  # vacio vs vacio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "lunar":  # vacio vs lunar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

    elif atacante.tipo == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "cometa":  # lunar vs cometa
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "volcanico":  # lunar vs volcanico
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)

        elif defensor.tipo == "estelar":  # lunar vs estelar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 0.5

        elif defensor.tipo == "vacio":  # lunar vs vacio
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)  * 1.5

        elif defensor.tipo == "lunar":  # lunar vs lunar
                defensor.HP_MAX -= (atacante.ataque-defensor.defensa)
