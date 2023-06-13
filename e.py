from EJ2_P1 import Vengadores
for personaje in Vengadores:
    if personaje["superheroe"] == "Vlanck Widow":
            personaje["superheroe"] = "Black Widow"
            break

print("Lista de personajes corregida:")
for personaje in Vengadores:
    print(personaje)