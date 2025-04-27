class producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock= stock

    def toDBColletion(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock
        }