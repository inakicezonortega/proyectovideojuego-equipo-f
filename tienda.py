
inventario = []
dinero_jugador = 100

class Tienda():

    def __init__(self, obj_disponibles):

        self.obj_disponibles = obj_disponibles


    def comprar(self, dinero_jugador, coste):

        while True:

            if len(self.obj_disponibles) > 0:       #Comprueba si hay objetos en la tienda

                # Mostrar items
                x = 1
                print("----------------------")
                for objeto in self.obj_disponibles:
                    print(x, ":", objeto, ", coste:", coste[x-1])
                    print("----------------------")
                    x += 1

                respuesta = input("¿Quieres comprar algo? \n Escribe si o no")

                if respuesta == "no": break

                elif respuesta == "si":
                    num = int(input("¿Que objeto quieres?"))

                    #Si el objeto SI esta en la tienda
                    if num >= 1 and num <= x:

                        #Si NO tiene dinero suficiente
                        if (dinero_jugador - coste[num-1]) < 0:
                            print ("No tienes dinero suficiente")

                        #Si tiene dinero suficiente
                        else:
                            print("Has añadido", self.obj_disponibles[num-1], "a tu inventario")
                            inventario.append(self.obj_disponibles[num-1])

                            dinero_jugador -= coste[num-1]
                            print ("Este es tu dinero restante:", dinero_jugador)

                            self.obj_disponibles.pop()[num-1]

                    #Si el objeto NO esta en la tienda
                    else: print ("Ese objeto no existe")
                else: print ("Escribe una respuesta valida")

            else:
                print ("No hay objetos en la tienda")
                break


def main():

    obj_disponibles = ["objeto1", "objeto2", "objeto3"]
    coste = [10, 15, 30]
    tienda = Tienda (obj_disponibles)
    tienda.mostrar(dinero_jugador, coste)


main()