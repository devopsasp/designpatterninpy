# Prototype class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")

# Concrete prototype classes
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("The cat meows.")

# Usage
dog = Dog("Fido")
dog.sound()  # Output: The dog barks.

cat = Cat("Whiskers")
cat.sound()  # Output: The cat meows.