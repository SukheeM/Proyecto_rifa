📄-Sistema de Sorteo en Python
¿Qué hace este programa?

Es un sorteo de 3 ganadores usando una lista de boletos.
Cada boleto tiene un número y está asignado a una persona.

La idea es:

Elegir 3 personas distintas al azar

Y a cada una asignarle uno de sus boletos, también al azar

📦 Datos de entrada

Los boletos están en un diccionario:

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


La clave es el número de boleto

El valor es la persona dueña de ese boleto

Una persona puede tener varios boletos

👥 Personas participantes
folk = list(set(boletos.values()))


Aquí se sacan las personas únicas, quitando duplicados.
Ojo: Python distingue mayúsculas y minúsculas, así que
"trikitrakatelas" y "Trikitrakatelas" cuentan como personas distintas.

✅ Validación básica
if len(folk) < 3:
    print("No hay suficientes personas para elegir 3 ganadores")


Si no hay al menos 3 personas diferentes, no se hace el sorteo.

🎲 Sorteo de ganadores
ganadores = random.sample(folk, 3)


Se eligen 3 personas sin repetir.
Todas tienen la misma probabilidad, sin importar cuántos boletos tengan.

🎟️ Elección del boleto ganador

Para cada persona ganadora:

Se buscan todos sus boletos

Se elige uno al azar

boletos_persona = [
    num for num, nombre in boletos.items() if nombre == persona
]
boleto_ganador = random.choice(boletos_persona)

🖨️ Resultado final

Se imprime algo como:

=== GANADORES ===
Persona: Ana | Boleto ganador: 10
Persona: Tania | Boleto ganador: 7
Persona: Manuel | Boleto ganador: 11
