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


#item1 = item('Mobile', 30000, 4)
#total = item1.calc_total_price()
#print(total)

#accessing class attributes
#print(item.pay_rate)

#discount_price = item1.apply_discount()
#print(f"Discounted Price : {discount_price}")

#print(item.__dict__) # All atributes of class
#print(item1.__dict__) # All atributes of instances

#item2 = item('Laptop', 100000, 5)
#item2.pay_rate = 0.6
#Laptop_discount_price = item2.apply_discount()
#print(Laptop_discount_price)

"""item3 = item("Cable", 10, 5)
item4 = item("Mouse", 50, 5)
item5 = item("Keyboard", 75, 5)"""

"""for instance in item.all:
    print(instance.name)"""

#print(item.all)

#item.instantiate_from_csv(r'C:\Users\NITRO\Data Science\item.csv')
#print(item.all)


class Phone(item): #Inheritance

    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):

        #Call super function to have access to all attributes / methods of the parent class
        super().__init__(
            name, price, quantity
        )


        # Run validations to received arguments 
        assert broken_phones >= 0, f"Broken Phones {broken_phones} must be greater than or equal to zero"

        # assigning instance attributes
        self.broken_phones = broken_phones


phone1 = Phone('Samsung M31', 5, 35000, 1)
#print(phone1.calc_total_price())
phone2 = Phone('Samsung A32', 3, 34500, 1)
#print(phone2.calc_total_price())
print(item.all) # better idea
print(Phone.all)