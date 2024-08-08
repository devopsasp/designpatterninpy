# Component interface
class Coffee:
    def cost(self):
        raise NotImplementedError

    def ingredients(self):
        raise NotImplementedError

# Concrete Component class
class SimpleCoffee(Coffee):
    def cost(self):
        return 1

    def ingredients(self):
        return "Coffee"

# Decorator abstract class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.decorated_coffee = coffee

    def cost(self):
        return self.decorated_coffee.cost()

    def ingredients(self):
        return self.decorated_coffee.ingredients()

# Concrete Decorator classes
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 0.5

    def ingredients(self):
        return super().ingredients() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 0.25

    def ingredients(self):
        return super().ingredients() + ", Sugar"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1

    def ingredients(self):
        return super().ingredients() + ", Whipped Cream"

# Client code
coffee = SimpleCoffee()
print(f"Cost: {coffee.cost()}; Ingredients: {coffee.ingredients()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"Cost: {coffee_with_milk.cost()}; Ingredients: {coffee_with_milk.ingredients()}")

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
print(f"Cost: {coffee_with_milk_and_sugar.cost()}; Ingredients: {coffee_with_milk_and_sugar.ingredients()}")

coffee_with_milk_sugar_and_whipped_cream = WhippedCreamDecorator(coffee_with_milk_and_sugar)
print(f"Cost: {coffee_with_milk_sugar_and_whipped_cream.cost()}; Ingredients: {coffee_with_milk_sugar_and_whipped_cream.ingredients()}")