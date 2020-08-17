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
        
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion, edad):
        Cuenta.__init__(self, titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

       



    def esTitularValido(self):
        if self.edad >=18 and self.edad <= 25:
            print("es titular valido")
            return True
        else:
            print("no es tiular")
            return False 

    def retirar(self, cantidad):
        if self.esTitularValido() == True:
            self.cantidad -= cantidad           
         
    def __str__(self):
        return "titular: {} bonificacion: {}".format(self.titular, self.bonificacion)     

    def mostrar(self):
        print(self.__str__())


#cuentaAdrian = Cuenta("Juan Perez")
#print(cuentaAdrian)
#cuentaAdrian.mostrar()
#cuentaAdrian.ingresar(100)
#cuentaAdrian.mostrar()
#cuentaAdrian.retirar(10)
#cuentaAdrian.mostrar()

prueba1 = CuentaJoven("Anto", 1500, 10, 20)
prueba1.esTitularValido()
prueba1.mostrar()

