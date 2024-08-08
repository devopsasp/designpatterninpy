class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def do_something(self):
        print("Doing something...")

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True

singleton1.do_something()  # Output: Doing something...
singleton2.do_something()  # Output: Doing something...