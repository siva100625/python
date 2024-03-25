"""print(1+2)
print('1'+'2')
print(int.__add__(1,2))
print(str.__add__("1","2"))

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return f"{self.r + other.r} + {self.i + other.i}i"

c1 = Complex(1, 2)
c2 = Complex(4, 6)
print(c1 + c2)
"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        if self.age>other.age:
            return True
        else:
            return False
        
p1=Person("S",18)
p2=Person("I",9)
if p1>p2:
    print(f"{p1.name}")
else:
    print(f"{p2.name}")

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return str(self.r + other.r) + " + " + str(self.i + other.i) + "i"

c1 = Complex(1, 2)
c2 = Complex(4, 6)
print(c1 + c2)


