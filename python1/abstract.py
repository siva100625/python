from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.no = n

    @abstractmethod
    def start(self): #abstract method
        pass       #no definition

    def display(self):#not a abstract method
        print("Hi")
