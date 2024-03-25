"""class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"HI {self.name} from student class")
s1=Student("Rahul")
print(s1.name)
s1.display() #Public


#protected _

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self._roll=rollno#protected
    def display(self):
        print(f"HI {self.name} from student class {self._roll}")
class Branch(Student):
    pass
def show():
     b1=Branch("Siva",8) 
     print(b1.name)
     print(b1._roll)

show()
s1=Student("siva",18)
s1.name="kkk"
s1._roll=48
s1.display()

#private __


class Student:
    def __init__(self,name,rollno,kk):
        self.name=name
        self._roll=rollno
        self.__age=kk
    def display(self):
        print(f"HI {self.name} from student class {self._roll}")
class Branch(Student):
    pass
def show():
     b1=Branch("Siva",8,80) 
     print(b1.name)
     print(b1._roll)

show()
s1=Student("siva",18,90)
s1.name="kkk"
s1._roll=48
print(s1.__age) #error cannot acces private outside the class
s1.display()



class Student:
    def __init__(self,name,rollno,kk):
        self.name=name
        self._roll=rollno
        self.__age=kk
    def display(self):
        print(f"HI {self.name} from student class {self._roll}")
class Branch(Student):
    def show(self):
        print(f"My age is {self.__age}") #error cannot acces private even in derived the class
def show():
     b1=Branch("Siva",8,80) 
     print(b1.name)
     print(b1._roll)

show()
s1=Student("siva",18,90)
s1.name="kkk"
s1._roll=48
print(s1.__age) #error cannot acces private outside the class
s1.display()

class Student:
    def __init__(self,name,rollno,kk):
        self.name=name
        self._roll=rollno
        self.__age=kk
    def display(self):
        print(f"HI {self.name} from student class {self._roll}")
    def priv(self):
        self.__display() #error 
class Branch(Student):
    def show(self):
        print(f"My age is {self.__age}") #error cannot acces private even in derived the class

s1=Student("siva",18,90)

s1.priv()
#name mangling
class Student:
    def __init__(self, name, rollno, kk):
        self.name = name
        self._roll = rollno
        self.__age = kk

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

# Accessing private attribute using name mangling
print(dir(s1))
print(s1._Student__age)
s1._Student__display()

# Error: 'Student' object has no attribute 'Student__display'
# s1.Student__display()
"""
