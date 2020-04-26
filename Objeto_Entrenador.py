import arcade
class Entrenador:
    def __init__(self, nombre):
        # String
        self.nombre = nombre
        # Int
        self.dinero = 0
        # Diccionario String-->Int
        self.inventario = {}
        # Lista de objetos Pokemon
        self.lista_equipo = []

    def restar_dinero(self, cantidad):
        self.dinero -= cantidad
        if self.dinero <= 0: self.dinero = 0

    def nuevo_pokemon(self, pokemon):
        self.lista_equipo.append(pokemon)
        if len(self.lista_equipo) >= 4:
            # En el caso de que nuestra lista de pokemons este llena tendra que aparecer un mensaje en pantalla que explique al jugador que debe
            # o cambiar uno de sus pokemons antiguo por el actual o desechar el actual y seguir con su equipo.
