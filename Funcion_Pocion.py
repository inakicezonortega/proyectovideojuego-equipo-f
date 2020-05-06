

def pocion(entrenador, vida_aliado, vida_maxima):

    while True:

        tipo_pocion = int(input("(1): Pocion \n (2): SuperPocion \n (3): MegaPocion \n (4): Cancelar"))

        if tipo_pocion == 1:

            if "pocion" in entrenador.inventario:

                if vida_aliado != vida_maxima:
                    entrenador.inventario.pop("pocion")
                    return (vida_aliado + (vida_aliado*0.25))

                else:
                    print ("Ya tienes la vida maxima")
                    break

            else:
                print("No te quedan pociones")
                break

        elif tipo_pocion == 2:

            if "superpocion" in entrenador.inventario:

                if vida_aliado != vida_maxima:
                    entrenador.inventario.pop("superpocion")
                    return (vida_aliado + (vida_aliado*0.5))

                else:
                    print ("Ya tienes la vida maxima")
                    break

            else:
                print ("No te quedan SuperPociones")
                break

        elif tipo_pocion == 3:

            if "megapocion" in entrenador.inventario:

                if vida_aliado != vida_maxima:
                    entrenador.inventario.pop("superpocion")
                    return (2 * vida_aliado)

                else:
                    print ("Ya tienes la vida maxima")
                    break

            else:
                print ("No te quedan MegaPociones")
                break

        elif tipo_pocion == 4: break

        else: print ("Elige una opcion valida")
