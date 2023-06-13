class BitacoraNave:
    def __init__(self):
        self.pila = []

    def mision(self, planeta, capturado, recompensa):
        self.pila.append((planeta, capturado, recompensa))

    def planetas_visitados(self):
        planetas_visitados = [mision[0] for mision in self.pila]
        return planetas_visitados

    def recaudacion_total(self):
        recaudacion_total = sum(mision[2] for mision in self.pila)
        return recaudacion_total

    def mision_han_solo(self):
        for i, mision in enumerate(self.pila):
            if mision[1] == "Han Solo":
                return i+1, mision[0]
        return None, None

bitacora = BitacoraNave()

bitacora.mision("Tatooine", "Han Solo", 18000)
bitacora.mision("Jakku", "Niima el Hutt", 1000)
bitacora.mision("Endor", "Ewoks", 200)
bitacora.mision("Naboo", "Jar Jar Binks", 1500)

planetas = bitacora.planetas_visitados()
print("Planetas visitados:", planetas)

recaudacion_total = bitacora.recaudacion_total()
print("La Recaudación total de Créditos Galácticos:", recaudacion_total)

num_mision, planeta = bitacora.mision_han_solo()
if num_mision is not None:
    print("Se capturó a Han Solo en la misión", num_mision, "en el planeta", planeta)
else:
    print("No se ha logrado capturar a Han Solo.")
