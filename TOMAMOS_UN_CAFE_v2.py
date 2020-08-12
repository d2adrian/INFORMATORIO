class Cafetera:
    def __init__(self, capacidadMaxima, cantidadActual=0):
        self.capacidadMaxima = capacidadMaxima
        self.cantidadActual = cantidadActual
    
    def __str__(self):
        return "La capacidad máxima es {}, y la cantidad actual es {}".format(self.capacidadMaxima, self.cantidadActual)

    def llenarCafetera(self):
        if (self.capacidadMaxima == self.cantidadActual):
            print("La cafetera esta llena.")
        else:
            self.cantidadActual = self.capacidadMaxima

    def servirTaza(self, capacidadTaza=0):
        self.capacidadTaza = capacidadTaza
        if (self.cantidadActual > self.capacidadTaza):
            self.cantidadActual -= self.capacidadTaza
            print("Se sirvio la taza con la cantidad {}".format(self.capacidadTaza))
        else:
            self.capacidadTaza = self.cantidadActual
            print("Se sirvió con lo que alcanzó")

    def vaciarCafetera(self):
        self.cantidadActual = 0
        print("La cantidad actual de café es: {}, se vació la cafetera".format(self.cantidadActual))

    def agregarCafe(self, agregar):
        self.agregar = agregar
        if self.cantidadActual < self.capacidadMaxima:
            self.cantidadActual += self.agregar
            print("La cantidad actual de la cafetera despues de agregar más es {}".format(self.cantidadActual))
        else:
            return
            



liliana = Cafetera(1000, 750)
print(liliana)
liliana.llenarCafetera()
print(liliana)
liliana.llenarCafetera()
liliana.servirTaza(250)
print(liliana)
liliana.servirTaza(500)
print(liliana)
liliana.servirTaza(350)
print(liliana)
liliana.vaciarCafetera()
print(liliana)
liliana.agregarCafe(500)
print(liliana)