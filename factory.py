# Define the factory class
from abc import ABC,abstractmethod
class VehicleFactory:
    def create_vehicle(self, type, brand, model):
        if type == 'car':
            return Car(brand, model)
        elif type == 'truck':
            return Truck(brand, model)
        else:
            raise ValueError(f"Unsupported vehicle type: {type}")

# Define the classes that the factory will create
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving a {self.brand} {self.model} car")

class Truck(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving a {self.brand} {self.model} truck")

# Usage example
factory = VehicleFactory()

my_car = factory.create_vehicle('car', 'Toyota', 'Corolla')
my_car.drive()  # Output: Driving a Toyota Corolla car

my_truck = factory.create_vehicle('truck', 'Ford', 'F-150')
my_truck.drive()  # Output: Driving a Ford F-150 truck