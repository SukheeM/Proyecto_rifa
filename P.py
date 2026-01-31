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
    print("=== GANADORES ===")
    
    for persona in ganadores:
        # Filtrar boletos de la persona
        boletos_persona = [num for num, nombre in boletos.items() if nombre == persona]
        
        # Seleccionar aleatoriamente un boleto de esa persona
        boleto_ganador = random.choice(boletos_persona)
        
        print(f"Persona: {persona} | Boleto ganador: {boleto_ganador}")


# TERMINADO 
