class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        if (self.price >= other.price):
            print(f"The item {self.item} is important than {other.item}")
            return True

        else:
            return False

        

O1 = Order("Milk", 35)
print(f"The Order is {O1.item}, the price is {O1.price}")

O2 = Order("Tofu", 53)
print(f"The Order is {O2.item}, the price is {O2.price}")

print(O1 > O2)
