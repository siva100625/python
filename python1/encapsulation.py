class Student:
    def __init__(self, name, rollno, kk):
        self.name = name
        self._roll = rollno
        self.__age = kk

    def get_age(self):
        return self.__age

    def set_age(self, age): #encapsulation hiding data from outside world
        if age > 25:
            print("Error: Age cannot be greater than 25")
        else:
            self.__age = age

    def display(self):
        print(f"HI {self.name} from student class {self._roll}")

    def priv(self):
        self.__display()  # error

    def __display(self):  # Define a private method
        print("This is a private method")


class Branch(Student):
    def show(self):
        print(f"My age is {self._Student__age}")  # Access private member


s1 = Student("siva", 18, 90)

# Accessing private attribute using getter method
print(s1.get_age())

# Modifying private attribute using setter method
s1.set_age(34)
print(s1.get_age())
