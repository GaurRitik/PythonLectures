class Product:
    prod_count = 0  # Class variable to keep track of total products across all stores
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.prod_count += 1  # Increment the class variable when a product is created

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}"   
    
    @classmethod
    def total_products(cls):
        return f"Total products across all stores: {cls.prod_count}"
    
    @staticmethod
    def calculate_discount(price, discount_percentage):
        discount_amount = price * (discount_percentage / 100)
        return price - discount_amount

p1 = Product("Laptop", 999.99)
p2 = Product("Smartphone", 499.49)
p3 = Product("Tablet", 299.99)

print(p1.display_info())
print(p2.display_info())
print(Product.total_products())
print(p3.display_info())
discounted_price = Product.calculate_discount(999.99, 10)
print(f"Discounted Price of Laptop: ${discounted_price:.2f}")
