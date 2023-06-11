class Car():
    def __init__(self, name, wheel):
        self.name=name
        self.wheel=wheel
        self.price=0
    def set_price(self, price):
        self.price=price
    def get_price(self):
        return self.price

    def details(self):
        print('This car name is ', self.name, 'and ', 'it has', self.wheel, 'wheel', 'price is', self.price)

