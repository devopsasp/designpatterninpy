class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, category={self.category})"

# Filter interface
class Filter:
    def filter(self, products):
        raise NotImplementedError("Method must be implemented.")

# Concrete filter classes
class PriceFilter(Filter):
    def __init__(self, max_price):
        self.max_price = max_price

    def filter(self, products):
        return [product for product in products if product.price <= self.max_price]

class CategoryFilter(Filter):
    def __init__(self, category):
        self.category = category

    def filter(self, products):
        return [product for product in products if product.category == self.category]

# Client code
products = [
    Product("Product A", 10.99, "Electronics"),
    Product("Product B", 5.99, "Clothing"),
    Product("Product C", 7.99, "Electronics"),
    Product("Product D", 12.99, "Home Goods"),
]

price_filter = PriceFilter(10.00)
category_filter = CategoryFilter("Electronics")

filtered_products = [product for product in products if product in price_filter.filter(products) and product in category_filter.filter(products)]

print(filtered_products)
# Output:
# [Product(name=Product A, price=10.99, category=Electronics), Product(name=Product C, price=7.99, category=Electronics)]