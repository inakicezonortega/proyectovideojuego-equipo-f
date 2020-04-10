import arcade
import ramdon
class Pokemon:
    def __init__(self,nombre,tipo,nivel,base_HP,base_stats,fijo):
        # String
        self.nombre = nombre
        self.tipo = tipo
        #Puntos de experiencia INT
        self.nivel = nivel
        self.contador_exp = 0
        self.exp_final = base_HP + nivel*fijo
        #Puntos de vida INT
        self.HP_MAX = base_HP + nivel*fijo
        self.HP = self.HP_MAX
        #Estadisticas daño y defensa INT
        self.ataque = base_stats + nivel*fijo
        self.defensa = base_stats + nivel*fijo
    #Definimos una serie de sets de las principales estadisticas de nuestra clase pokemon
    def set_exp_final(self,nivel):
        self.exp_final =  base_HP + nivel*fijo

    def set_HP_MAX(self,nivel):
        self.HP_MAX = base_HP + nivel*fijo
    def sumar_HP_MAX(self,cantidad):
        self.HP_MAX +=cantidad

    def set_ataque(self,nivel):
        self.ataque = base_stats + nivel*fijo
    def sumar_ataque(self,cantidad):
        self.ataque += cantidad

    def set_defensa(self,nivel):
        self.defensa = base_stats + nivel*fijo
    def sumar_defensa(self,cantidad):
        self.defensa += cantidad
    # Definimos las funciones principales relacionado con HP
    def sumar_HP(self,cantidad):
        self.HP +=cantidad
        if self.HP>self.HP_MAX:
            self.HP = self.HP_MAX
    def restar_HP(self,cantidad):
        self.HP -= cantidad
        if self.HP<0:
            self.HP = 0

    def subir_nivel(self):
        self.nivel +=1
        self.contador_exp = 0;
        set_exp_final(self.nivel)
        set_HP_MAX(self.nivel)
        sumar_HP(self.HP_MAX)
        set_ataque(self.nivel)
        set_defensa(self.nivel)
        return "Has subido de nivel"