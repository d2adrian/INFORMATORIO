class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    def __str__(self):
        return "titular: {} cantidad: {}".format(self.titular, self.cantidad)     

    def mostrar(self):
        print(self.__str__())

    def ingresar(self,cantidad):
        if cantidad < 0:
            return
        else:
            self.cantidad += cantidad  

    def retirar(self, cantidad):
        self.cantidad -= cantidad              
        



cuentaAdrian = Cuenta("Juan Perez")
print(cuentaAdrian)
cuentaAdrian.mostrar()
cuentaAdrian.ingresar(100)
cuentaAdrian.mostrar()
cuentaAdrian.retirar(10)
cuentaAdrian.mostrar()

