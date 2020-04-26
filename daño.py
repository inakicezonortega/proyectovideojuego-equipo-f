


    def atacar(self,ataque,hp_enemigo, def_enemigo, tipo_enemigo,tipo_aliado):
        hp_total = hp_enemigo + def_enemigo

        if tipo_aliado == "demonio":
            if tipo_enemigo== "demonio": # demonio vs demonio
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "cometa": # demonio vs cometa
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "volcanico": # demonio vs volcanico
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "estelar": # demonio vs estelar
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "vacio":  # demonio vs vacio
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "lunar": # demonio vs lunar
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

        elif tipo_aliado == "cometa":
            if tipo_enemigo== "demonio": #cometa vs demonio
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "cometa": #cometa vs cometa
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "volcanico": #cometa vs volcanico
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "estelar": #cometa vs estelar
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "vacio":  # cometa vs vacio
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "lunar": #cometa vs lunar
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

        elif tipo_aliado == "volcanico":
            if tipo_enemigo== "demonio": # volcanico vs demonio
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "cometa": #volcanico vs cometa
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "volcanico": #volcanico vs volcanico
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "estelar": #volcanico vs estelar
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "vacio":  #volcanico vs vacio
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "lunar": #volcanico vs lunar
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

        elif tipo_aliado == "estelar":
            if tipo_enemigo== "demonio": #estelar vs demonio
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "cometa":#estelar vs cometa
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "volcanico":#estelar vs volcanico
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "estelar":#estelar vs  estelar
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "vacio":  # estelar vs vacio
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "lunar": #estelar vs  lunar
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

        elif tipo_aliado == "vacio":
            if tipo_enemigo == "demonio":  # vacio vs demonio
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "cometa":  # vacio vs cometa
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "volcanico":  # vacio vs volcanico
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "estelar":  # vacio vs estelar
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "vacio":  # vacio vs vacio
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "lunar":  # vacio vs lunar
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

        elif tipo_aliado == "lunar":
             if tipo_enemigo== "demonio": #lunar vs demonio
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "cometa": #lunar vs cometa
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "volcanico": #lunar vs volcanico
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo-1
                else: return hp_total - ataque

            elif tipo_enemigo == "estelar": #lunar vs estelar
                if hp_enemigo > hp_total - ataque*0.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*0.5

            elif tipo_enemigo == "vacio": #lunar vs vacio
                if hp_enemigo > hp_total - ataque*1.5:
                    return hp_enemigo-1
                else: return hp_total - ataque*1.5

            elif tipo_enemigo == "lunar": #lunar vs lunar
                if hp_enemigo > hp_total - ataque:
                    return hp_enemigo - 1
                else:
                    return hp_total - ataque