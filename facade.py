# Subsystem classes
class CPU:
    def freeze(self):
        print("CPU: Freezing...")

    def jump(self, address):
        print(f"CPU: Jumping to address {address}...")

    def execute(self):
        print("CPU: Executing...")


class Memory:
    def load(self, address, data):
        print(f"Memory: Loading data '{data}' into address {address}...")


class HardDrive:
    def read(self, address):
        print(f"HardDrive: Reading data from address {address}...")
        return "Data from hard drive"


# Facade class
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        data = self.hard_drive.read("Boot Address")
        self.memory.load("Boot Address", data)
        self.cpu.jump("Boot Address")
        self.cpu.execute()


# Client code
computer = Computer()
computer.start_computer()