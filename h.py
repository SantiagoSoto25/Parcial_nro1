from EJ2_P1 import Vengadores
nuevos_superheroes = [
    {
        "superheroe": "Spider-Man",
        "personaje": "Peter Parker",
        "grupo": "Avengers",
        "aparicion": 1962
    },
    {
        "superheroe": "Black Widow",
        "personaje": "Natasha Romanoff",
        "grupo": "Avengers",
        "aparicion": 1964
    },
    {
        "superheroe": "Hulk",
        "personaje": "Bruce Banner",
        "grupo": "Avengers",
        "aparicion": 1962
    },
    {
        "superheroe": "Thor",
        "personaje": "",
        "grupo": "Avengers",
        "aparicion": 1962
    },
    {
        "superheroe": "Wolverine",
        "personaje": "Logan",
        "grupo": "",
        "aparicion": 1974
    },
    {
        "superheroe": "Black Panther",
        "personaje": "T'Challa",
        "grupo": "",
        "aparicion": 1966
    },
    {
        "superheroe": "Doctor Strange",
        "personaje": "Stephen Strange",
        "grupo": "",
        "aparicion": 1963
    },
    {
        "superheroe": "Captain Marvel",
        "personaje": "Carol Danvers",
        "grupo": "",
        "aparicion": 1968
    },
    {
        "superheroe": "Ant-Man",
        "personaje": "Scott Lang",
        "grupo": "",
        "aparicion": 1962
    },
    {
        "superheroe": "Hawkeye",
        "personaje": "Clint Barton",
        "grupo": "",
        "aparicion": 1964
    },
    {
        "superheroe": "Scarlet Witch",
        "personaje": "Wanda Maximoff",
        "grupo": "",
        "aparicion": 1964
    },
    {
        "superheroe": "Vision",
        "personaje": "",
        "grupo": "",
        "aparicion": 1968
    },
    {
        "superheroe": "Falcon",
        "personaje": "Sam Wilson",
        "grupo": "Avengers",
        "aparicion": 1969
    },
    {
        "superheroe": "Winter Soldier",
        "personaje": "Bucky Barnes",
        "grupo": "Avengers",
        "aparicion": 2005
    },
    {
        "superheroe": "War Machine",
        "personaje": "James Rhodes",
        "grupo": "Avengers",
        "aparicion": 1979
    },
    {
        "superheroe": "Black Panther",
        "personaje": "Shuri",
        "grupo": "",
        "aparicion": 2005
    },
    {
        "superheroe": "Doctor Strange",
        "personaje": "Wong",
        "grupo": "",
        "aparicion": 1963
    },
    {
        "superheroe": "Spider-Woman",
        "personaje": "Jessica Drew",
        "grupo": "",
        "aparicion": 1977
    },
    {
        "superheroe": "She-Hulk",
        "personaje": "Jennifer Walters",
        "grupo": "",
        "aparicion": 1980
    },
    {
        "superheroe": "Namor",
        "personaje": "",
        "grupo": "",
        "aparicion": 1939
    }
]

for nuevo_superheroe in nuevos_superheroes:
    existe = False
    for personaje in Vengadores:
        if personaje["superheroe"] == nuevo_superheroe["superheroe"]:
            existe = True
            break
    if not existe:
        Vengadores.append(nuevo_superheroe)

print("Lista de personajes actualizada:")
for personaje in Vengadores:
    print(personaje)