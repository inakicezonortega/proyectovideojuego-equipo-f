def stat_ataque(ataque):
    ataque = ataque + (ataque * 0.23)
    
    return ataque

def stat_vida(vida):
    vida = vida + (vida * 0.205)

    return vida

def stat_defensa(defensa):
    defensa = defensa + (defensa * 0.27)

    return defensa

def exp(exp_actual,lvl_aliado,lvl_enemigo):

    dif_nivel = lvl_aliado - lvl_enemigo
    if dif_nivel == 0:
        exp_actual = exp_actual +  8
    elif dif_nivel > 0:
        exp_actual = exp_actual + 5
    elif dif_nivel < 0:
        exp_actual = exp_actual + 13

    return exp_actual
lvl_aliado = 6
lvl_enemigo = 4
exp_actual = 0
exp_final = 50
vida = 22
ataque = 9
defensa = 4
i = 0
for i in range (9):
    
    ataque = stat_ataque(ataque)
    vida = stat_vida(vida)
    defensa = stat_defensa(defensa)
    vida_resultado = (ataque - defensa) * 0.5
    print("vida:",vida,"ataque:",ataque,"defensa:",defensa)

for i in range (30):

    ataque = ataque + 3
    vida = vida + 5
    defensa = defensa + 2
    print("vida:",vida,"ataque:",ataque,"defensa:",defensa)

exp_actual = exp(exp_actual,lvl_aliado,lvl_enemigo)
print("exp actual:",exp_actual)



