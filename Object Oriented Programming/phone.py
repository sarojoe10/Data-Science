from Item import item

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