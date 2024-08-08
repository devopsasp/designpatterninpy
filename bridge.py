# Abstraction
class Vehicle:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        self.implementation.operation_implementation()

# Refined Abstraction
class Car(Vehicle):
    def __init__(self, implementation):
        super().__init__(implementation)

    def assemble(self):
        print("Assembling a car...")
        self.operation()

class Truck(Vehicle):
    def __init__(self, implementation):
        super().__init__(implementation)

    def assemble(self):
        print("Assembling a truck...")
        self.operation()

# Implementation
class Production:
    def operation_implementation(self):
        print("Producing a vehicle...")

class Testing:
    def operation_implementation(self):
        print("Testing a vehicle...")

# Usage
car_production = Car(Production())
car_production.assemble()
# Output:
# Assembling a car...
# Producing a vehicle...

truck_testing = Truck(Testing())
truck_testing.assemble()
# Output:
# Assembling a truck...
# Testing a vehicle...