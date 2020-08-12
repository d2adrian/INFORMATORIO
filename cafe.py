class Cafetera:
    def __init__(self, capacidadMaxima, cantidadActual = 0):
        self.capacidadMaxima = capacidadMaxima
        self.cantidadActual = cantidadActual
    
    def __str__(self):
        return "La capacidad máxima es {}, y la cantidad actual es {}".format(self.capacidadMaxima, self.cantidadActual)

    def llenarCafetera(self):
        if (self.capacidadMaxima == self.cantidadActual):
            print("La cafetera esta llena.")
        else:

            self.cantidadActual = self.capacidadMaxima

    def servirTaza(self, taza = 0):
        self.taza = taza
        if (self.cantidadActual > self.taza):
            self.cantidadActual -= self.taza
        else:
            self.taza = self.cantidadActual

philip = Cafetera(1500,0)
print(philip)
philip.llenarCafetera()
print(philip)
philip.llenarCafetera()
philip.servirTaza(250)
print(philip)