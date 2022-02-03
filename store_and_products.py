class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        self.products.pop(id)
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.price += percent_increase * product.price
            return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.price -= percent_discount * product.price
                return self

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price * percent_change
            print(self.price)
        else:
            self.price -= self.price * percent_change
            print(self.price)
        return self

    def print_info(self):
        print(f"Product: {self.name}\nCategory: {self.category}\nPrice: ${self.price}")
        return self

Desserts = ["ice cream", "chocolate", "cake"]
Target = Store("Target")
Carrots = Product("carrots", 10, "vegetables")
Pineapple = Product("pineapple", 20, "fruit")