print("Date:13-04-2026")
print("UIN:251A025")
# Product Class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


# Customer Class
class Customer:
    def __init__(self, name):
        self.name = name


# Cart Class
class Cart:
    def __init__(self, customer):
        self.items = []
        self.total = 0
        self.customer = customer   # store customer

    def add(self, product, qty):
        if product.stock >= qty:
            self.items.append((product, qty))
            print(product.name, "added")
        else:
            print("Not enough stock")

    def calculate_total(self):
        self.total = 0
        for product, qty in self.items:
            self.total += product.price * qty
        return self.total

    def place_order(self):
        print("\nCustomer:", self.customer.name)   # print customer name
        for product, qty in self.items:
            product.stock -= qty
        print("Order placed")


# Main Program
p1 = Product("Laptop", 50000, 5)
p2 = Product("Mobile", 20000, 10)

customer = Customer("Komal")

cart = Cart(customer)   # pass customer

cart.add(p1, 1)
cart.add(p2, 2)

print("Total Cost:", cart.calculate_total())

cart.place_order()

print("\nRemaining Stock:")
print(p1.name, p1.stock)
print(p2.name, p2.stock)
