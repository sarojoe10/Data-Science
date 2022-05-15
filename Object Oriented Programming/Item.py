import csv

class item:

    
    pay_rate = 0.8 # class attributes

    all = []

    def __init__(self, name: str, price: int, quantity=0):

        # Actions to execute
        item.all.append(self)

        # Run validations to received arguments 
        assert price >= 0 , f"Price { price } must be greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} must be greater than or equal to zero"

        # assigning instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity
        
        

    def calc_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate # using class atribute, can also use instance atribute as self.pay_rate instead which is better practice

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for Item in items:
            item(name=Item.get('name'),
                price=float(Item.get('price')),
                quantity=int(Item.get('quantity'))
            
            )

    @staticmethod
    def is_integer(num):
        # We will check whether passed num is integer
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False 

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
