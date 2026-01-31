import random

boletos = {
    1: "Limon",
    2: "Limon",
    3: "trikitrakatelas",
    4: "toño",
    5: "Trikitrakatelas",
    6: "Manuel",
    7: "Tania",
    8: "Tania",
    9: "Ana",
    10: "Ana",
    11: "Manuel",
    12: "Paty"

}

folk = list(set(boletos.values()))

# Verificacion de si hay minimo 3 personas
if len(folk) < 3:
    print("No hay suficientes personas para elegir 3 ganadores")
else:
    ganadores = random.sample(folk, 3)

# ya nada mas aqui ponle que itere en la lista de ganadores obtenida en el else 
#que se identifiquen los boletos que son de la misma persona poara que no pueda ganr dos veces 
#que se selecione aleatoriamente uno de los boletos y muestre el nombre de la persona con el numero del boleto ganador
