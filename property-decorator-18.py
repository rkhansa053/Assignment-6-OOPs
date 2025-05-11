class Product:
    def __init__(self, name, price):
        self.name= name
        self.price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price


# ACCESSING THE PRICE USING THE @PROPERTY
product = Product("LAPTOP", 19900)
print(product.price)

# UPDATING PRICE USING THE @PRICE.SETTER
product.price = 20000
print(product.price)

# TRYING TO SET A NEGATIVE PRICE
product.price = -500

# DELETING THE PRICE 
del product.price
