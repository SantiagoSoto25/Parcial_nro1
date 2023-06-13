from EJ2_P1 import Vengadores
buscar_personaje = "Capitana Marvel"
nombre_personaje = None

for personaje in Vengadores:
    if personaje["superheroe"] == buscar_personaje:
        nombre_personaje = personaje["personaje"]
        break
if nombre_personaje:
    print(f"El nombre de personaje de '{buscar_personaje}' es: {nombre_personaje}")
else:
    print(f"No se encontró el personaje '{buscar_personaje}' en la lista.")