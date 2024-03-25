"""class Human:
    def eat(self):
        print("U can eat")
class Male(Human):
    def sleep(self):
        print("sls")
class Female(Human):
    def work(self):
        print("work")

f1=Female()
f1.eat()
m1=Male()
m1.eat()

class Human:
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def display(self):
        print(f"Your {self.nam} and my age is {self.ag}")
    def eat(self):
        print("U can eat")
class Male(Human):
    def sleep(self):
        print("sls")
class Female(Human):
    def work(self):
        print("work")

f1=Female("riya",18)
f1.eat()
m1=Male("siva",18)
m1.eat()
m1.display()

class Human:
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def display(self):
        print(f"Your {self.nam} and my age is {self.ag}")
    def eat(self):
        print("U can eat")
class Male(Human):
    def __init__(self, m_name, age,l):
        Human.__init__(self,m_name,age)
        self.lo=l
    def sleep(self):
        print("sls")
class Female(Human):
    def __init__(self, name, age,candance):
        super().__init__(name, age)
        self.ca=candance

    def show(self):
        Human.display(self)
        print(f"dance:{self.ca}")

    def work(self):
        print("work")

f1=Female("riya",18,True)
f1.eat()

m1=Male("siva",18,"tuty")
m1.eat()
m1.display()
f1.display()
print(m1.lo)
print(f1.ca)
f1.show()"""

class Person:
    cls=0
    def work(self):
        print("work")
class Student(Person):
    d=0
    def dark(self):
        print("Dark")
class Faculty(Person):
    e=0
    def dam(self):
        print("l")

s=Student()
f=Faculty()
s.work()
print(s.cls)
print(s.d)
f.work()
print(f.cls)
print(f.e)