class Product:
    def __init__(self, initial_name, initial_price, initial_quantity):
        self.name = initial_name
        self.price = initial_price
        self.quantity = initial_quantity

    def print_product(self):
        print(self.name + ", price " + str(self.price) + ", " + str(self.quantity) + " pcs")
