
class Ataque():

    def __init__(self, nombre, daño, tipo):
        "Constructor"

        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo


    def atacar(self,hp_enemigo, def_enemigo, tipo_enemigo):   # agua > fuego > planta > agua

        hp_total = hp_enemigo + def_enemigo

        if self.tipo == "agua":
            if tipo_enemigo == "agua":                  #agua vs agua
                return hp_total - self.daño
            if tipo_enemigo == "fuego":                 #agua vs fuego
                return hp_total - (self.daño + 10)
            else:                                       #agua vs planta
                return hp_total - (self.daño - 5)

        if self.tipo == "fuego":
            if tipo_enemigo == "fuego":                 #fuego vs fuego
                return hp_total - self.daño
            if tipo_enemigo == "planta":                #fuego vs planta
                return hp_total - (self.daño + 10)
            else:                                       #fuego vs agua
                return hp_total - (self.daño - 5)

        if self.tipo == "planta":
            if tipo_enemigo == "planta":                #planta vs planta
                return hp_total - self.daño
            if tipo_enemigo == "agua":                  #planta vs agua
                return hp_total - (self.daño + 10)
            else:                                       #planta vs fuego
                return hp_total - (self.daño - 5)


    def imprimir_datos(self):

        print ("Nombre: ", self.nombre, "\n Daño: ", self.daño, "\n Tipo: ", self.tipo)

def main():

    ataque1 = Ataque ("nombre1", 10, "fuego")
    ataque1.imprimir_datos()
    print (ataque1.atacar(100,10, "agua"))

main()