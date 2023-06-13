def contar_palabra (palabra, vector):
    if len(vector) == 0:
        return 0
    if vector[0] == palabra:
        return 1 + contar_palabra(palabra, vector[1:])
    else:
        return contar_palabra(palabra, vector[1:])

vector = ["Goku", "Vegeta", "Gohan", "Goku", "Vegito", "Vegito", "Goku"]
personaje = "Vegito"

contador = contar_palabra(personaje, vector)
print(f"El personaje '{personaje}' aparece {contador} veces en tu camino..")
