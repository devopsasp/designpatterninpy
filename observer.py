# Observer interface
class Observer:
    def update(self, data):
        raise NotImplementedError('Observer must implement update method')


# Concrete observers
class ConcreteObserverA(Observer):
    def update(self, data):
        print(f'Observer A received data: {data}')


class ConcreteObserverB(Observer):
    def update(self, data):
        print(f'Observer B received data: {data}')


# Subject
class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)


# Client code
subject = Subject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.add_observer(observer_a)
subject.add_observer(observer_b)

subject.notify('Hello, world!')  # Output:
# Observer A received data: Hello, world!
# Observer B received data: Hello, world!

subject.remove_observer(observer_a)
subject.notify('Goodbye, world!')  # Output:
# Observer B received data: Goodbye, world!