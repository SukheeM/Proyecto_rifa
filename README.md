📄-Sistema de Sorteo en Python
1. Descripción general

Este programa realiza un sorteo aleatorio de ganadores a partir de un conjunto de boletos asociados a distintas personas.
El objetivo es seleccionar 3 personas ganadoras distintas y asignar a cada una uno de sus boletos de manera aleatoria.

El sistema está diseñado para garantizar que:

No se repitan personas ganadoras.

Cada ganador tenga exactamente un boleto asignado.

El sorteo solo se realice si hay al menos 3 personas distintas.

2. Estructura de datos
Diccionario boletos
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


Clave (key): número de boleto (entero).

Valor (value): nombre de la persona propietaria del boleto (cadena de texto).

Una persona puede tener uno o varios boletos.

3. Obtención de personas únicas
folk = list(set(boletos.values()))


boletos.values() obtiene todos los nombres.

set() elimina duplicados.

list() convierte el conjunto en una lista utilizable.

📌 Nota importante:
Python distingue entre mayúsculas y minúsculas, por lo que:

"trikitrakatelas" y "Trikitrakatelas" se consideran personas distintas.

4. Validación de participantes mínimos
if len(folk) < 3:
    print("No hay suficientes personas para elegir 3 ganadores")


Se verifica que existan al menos 3 personas distintas.

Si no se cumple la condición, el sorteo no se realiza.

5. Selección de ganadores
ganadores = random.sample(folk, 3)


random.sample() selecciona 3 personas distintas al azar.

Todas las personas tienen la misma probabilidad de ser elegidas, sin importar cuántos boletos tengan.

6. Asignación del boleto ganador
boletos_persona = [
    num for num, nombre in boletos.items() if nombre == persona
]
boleto_ganador = random.choice(boletos_persona)


Para cada persona ganadora:

Se filtran todos los boletos que le pertenecen.

Se elige un boleto al azar de esa lista.

Se muestra el resultado en pantalla.

7. Salida del programa

Ejemplo de salida:

=== GANADORES ===
Persona: Ana | Boleto ganador: 9
Persona: Manuel | Boleto ganador: 6
Persona: Tania | Boleto ganador: 8

8. Consideraciones importantes

🔹 El sorteo es por persona, no por boleto.

🔹 Tener más boletos no aumenta la probabilidad de ganar.

🔹 Una persona no puede ganar más de una vez.

🔹 El sistema es completamente aleatorio.

9. Posibles mejoras futuras

Normalizar nombres (mayúsculas/minúsculas).

Realizar el sorteo por boleto en lugar de por persona.

Guardar los resultados en un archivo.

Evitar que una persona gane en sorteos consecutivos.
