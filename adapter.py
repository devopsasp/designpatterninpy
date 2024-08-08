# Target interface
class Duck:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("I'm flying!")

# Adaptee interface
class Turkey:
    def gobble(self):
        print("Gobble!")

    def fly_short_distance(self):
        print("I'm flying a short distance!")

# Adapter class
class TurkeyAdapter:
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(5):
            self.turkey.fly_short_distance()

# Client code
turkey = Turkey()
turkey_adapter = TurkeyAdapter(turkey)

turkey_adapter.quack()  # Output: Gobble!
turkey_adapter.fly()  # Output: I'm flying a short distance! (5 times)