class Order:
    def __init__(self):
        self.list =[]

    def total_price(self):
        self.total = sum([item.subtotal for item in self.list])
        return self.total

    def discount(self, discount):
        self.total = sum([item.subtotal for item in self.list])
        self.total -= self.total * (discount / 100)
        return self.total

    def add_item(self, item):
        self.list.append(item)

    def get_list(self):
        print("Nombre                 Precio")
        for item in self.list:
            print(f"{item.name} x {item.quantity}    {item.price}")


class MenuItem:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal= self.price*self.quantity

class Juice(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.sugar=sugar

class Soup(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind
        
class Soda(MenuItem):
    def __init__(self, name, price,quantity,sugar):
        super().__init__(name, price,quantity)
        self.sugar=sugar
        
class IceCream(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.sugar=kind
        
class Beer(MenuItem):
    def __init__(self, name, price,quantity,brand):
        super().__init__(name, price,quantity)
        self.brand=brand
        
class Sandiwch(MenuItem):
    def __init__(self, name, price,quantity,protein):
        super().__init__(name, price,quantity)
        self.protein=protein
        
class MainDish(MenuItem):
    def __init__(self, name, price,quantity,description):
        super().__init__(name, price,quantity)
        self.description=description
        
class Beef(MenuItem):
    def __init__(self, name, price,quantity,grams):
        super().__init__(name, price,quantity)
        self.grams=grams
        
class SideDish(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind
        
class Appetizer(MenuItem):
    def __init__(self, name, price,quantity,kind):
        super().__init__(name, price,quantity)
        self.kind=kind

orden=Order()

orden.add_item(Juice(name="Jugo de mango",price=2000,quantity=3,sugar="No"))
orden.add_item(Soup(name="Sancocho de pescado",price=4000,quantity=2,kind="Sancocho"))
orden.add_item(MainDish(name="Cerdo a la llanera",price=9000,quantity=2,description="Cerdo con salsa de la casa, arroz, patacon y ensalada"))
orden.add_item(Appetizer(name="Parfait",price=3500,quantity=2,kind="Dulce"))

print("El precio total de la orden es:" + str(orden.total_price()))
orden.get_list()
