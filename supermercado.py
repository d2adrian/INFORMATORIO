#Un supermercado maneja el catálogo de los productos que vende. De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no. Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

#Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad. Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%. Es decir:

#precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9

#El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de productos que comercializa y la suma total de los precios de los mismos.

#Gracias a anto, dana, violeta, tomaron la decision sin consultar a los varones de que solamente existe un solo catalogo global xd

#Espacio de clases

 # -*- coding: utf-8 -*-



from os import system  #esto es para que
system("cls")        #limpie la consola

class supermercado:
    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.catalogo = list()
        
        self.__precio = 0

    def __repr__(self):
        return "{}".format(self.catalogo)
    
    def agregarProducto(self, producto):
        #producto3 = producto(marca, tipo, precio, precioCuidado, primeraNecesidad)
        #self.__producto = producto(marca, tipo, precio, precioCuidado, primeraNecesidad)
        self.catalogo.append(producto)

    def cantidadTotalProductos(self):
        print("Cantidad total de productos: ",len(self.catalogo))

    def precioTotalProductos(self):
        for x in self.catalogo:
            self.__precio = self.__precio + x.precio
        print("Precio total de productos: ",self.__precio)

class producto:
    def __init__(self, marca, tipo, precio, precioCuidado = False, primeraNecesidad = False):
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.precioCuidado = precioCuidado
        self.primeraNecesidad = primeraNecesidad

    def __repr__(self):
        return "\nMarca: {}\nTipo: {}\nPrecio: {}\nPrecioCuidado: {}\nPrimera necesidad: {}\n".format(self.marca, self.tipo,self.precio, self.precioCuidado, self.primeraNecesidad)

#CODIGO PRINCIPAL

supermercado1 = supermercado('Carrefour','Av. San Martin 446')
supermercado1.agregarProducto(producto('Serenisima', 'Leche',70,True,True))
supermercado1.agregarProducto(producto('Sancor', 'Yogur',90,True,True))
supermercado1.agregarProducto(producto('Coca Cola', 'Gaseosa',120))
supermercado1.agregarProducto(producto('Pepsi', 'Gaseosa',130))
supermercado1.agregarProducto(producto('Paladini', 'Salchicha',35))
supermercado1.agregarProducto(producto('Blanca Flor', 'Harina',45,True,True))
supermercado1.agregarProducto(producto('Ace', 'Azucar',60))
supermercado1.agregarProducto(producto('Ala', "Jabon en Polvo",40))
print(supermercado1)
supermercado1.cantidadTotalProductos()
supermercado1.precioTotalProductos()






"""producto1 = producto('Coca Cola', 'Gaseosa', 120)
print(producto1)
producto2= producto('Serenisima', 'Leche',70,True,True)
print(producto2)"""
