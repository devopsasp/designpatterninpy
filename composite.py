from abc import ABC, abstractmethod

# Abstract Component class
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf Node class
class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"Leaf {self.name} operation")

# Composite Node class
class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print(f"Composite {self.name} operation")
        for child in self.children:
            child.operation()

# Client code
root = Composite("Root")
leaf1 = Leaf("Leaf 1")
leaf2 = Leaf("Leaf 2")
leaf3 = Leaf("Leaf 3")

root.add(leaf1)
root.add(leaf2)

subcomposite = Composite("Subcomposite")
subcomposite.add(leaf3)

root.add(subcomposite)

root.operation()