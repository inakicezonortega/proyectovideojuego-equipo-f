
class Ataque():

    def __init__(self, nombre, daño):
        "Constructor"
        self.nombre = nombre
        self.daño = daño

    def atacar(self,hp_enemigo, def_enemigo, tipo_enemigo,tipo_aliado):
        hp_total = hp_enemigo + def_enemigo

        if tipo_aliado == "agua":
            if tipo_enemigo == "agua":                  #agua vs agua
                return hp_total - self.daño
            if tipo_enemigo == "fuego":                 #agua vs fuego
                return hp_total - self.daño*1.5
            else:                                       #agua vs planta
                return hp_total - self.daño*0.5

        if tipo_aliado == "fuego":
            if tipo_enemigo == "fuego":                 #fuego vs fuego
                return hp_total - self.daño
            if tipo_enemigo == "planta":                #fuego vs planta
                return hp_total - self.daño*1.5
            else:                                       #fuego vs agua
                return hp_total - self.daño*0.5

        if tipo_aliado == "planta":
            if tipo_enemigo == "planta":                #planta vs planta
                return hp_total - self.daño
            if tipo_enemigo == "agua":                  #planta vs agua
                return hp_total - self.daño*1.5
            else:                                       #planta vs fuego
                return hp_total - self.daño*0.5


    def imprimir_datos(self):

        print ("Nombre: ", self.nombre, "\n Daño: ", self.daño, "\n Tipo: ", self.tipo)

