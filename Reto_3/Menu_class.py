class Order:
    def __init__(self):
        self.list =[]

    def total_price(self):
        self.total = sum([item.price * item.quantity for item in self.items])
        return self.total

    def discount(self, discount):
        self.total -= self.total * (discount / 100)
        return self.total

    def add_item(self, item):
        self.items.append(item)

    def show_order(self):
        return self.list


class MenuItem:
    def __init__(self, name, price,quantity,):
        self.name = name
        self.price = price
        self.quantity = quantity


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
