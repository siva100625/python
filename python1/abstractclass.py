import abstract

class Bike(abstract.Vehicle):
    def __init__(self, n, color):
        super().__init__(n)
        self.color = color

    def start(self):
        print("Start with kick")

    def display(self):
        print(f"My color is {self.color}")

class Scooty(abstract.Vehicle):
    def __init__(self, n):
        self.n = n

    def start(self):
        print("Self start")


