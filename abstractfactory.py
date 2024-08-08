from abc import ABC, abstractmethod

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

# Abstract Products
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Concrete Products
class ProductA1(AbstractProductA):
    def operation_a(self):
        print("Product A1 operation")

class ProductB1(AbstractProductB):
    def operation_b(self):
        print("Product B1 operation")

class ProductA2(AbstractProductA):
    def operation_a(self):
        print("Product A2 operation")

class ProductB2(AbstractProductB):
    def operation_b(self):
        print("Product B2 operation")

# Client code
def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    product_a.operation_a()
    product_b.operation_b()

# Usage
factory1 = ConcreteFactory1()
client_code(factory1)  # Output: Product A1 operation, Product B1 operation

factory2 = ConcreteFactory2()
client_code(factory2)  # Output: Product A2 operation, Product B2 operation