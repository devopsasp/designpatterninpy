# Product class
class Car:
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = ""
        self.color = ""

    def set_make(self, make):
        self.make = make
        return self

    def set_model(self, model):
        self.model = model
        return self

    def set_year(self, year):
        self.year = year
        return self

    def set_color(self, color):
        self.color = color
        return self

    def __str__(self):
        return f"Car: {self.make} {self.model} {self.year} {self.color}"

# Builder class
class CarBuilder:
    def __init__(self):
        self.car = Car()

    def with_make(self, make):
        self.car.set_make(make)
        return self

    def with_model(self, model):
        self.car.set_model(model)
        return self

    def with_year(self, year):
        self.car.set_year(year)
        return self

    def with_color(self, color):
        self.car.set_color(color)
        return self

    def build(self):
        return self.car

# Director class
class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.with_make("Porsche").with_model("911").with_year("2022").with_color("Red")
        return self.builder.build()

    def construct_family_car(self):
        self.builder.with_make("Toyota").with_model("Camry").with_year("2020").with_color("Silver")
        return self.builder.build()

# Usage
builder = CarBuilder()
director = CarDirector(builder)

sports_car = director.construct_sports_car()
print(sports_car)  # Output: Car: Porsche 911 2022 Red

family_car = director.construct_family_car()
print(family_car)  # Output: Car: Toyota Camry 2020 Silver