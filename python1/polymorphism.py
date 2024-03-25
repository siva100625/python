"""def square(x): #dynamic typing
    return x*x
print(square(5))"""

"""float square(float x)#static typing
{
    return x*x
}
int square(int x)#static typing
{
    return x*x
}"""
#duck typing
"""class Duck:
    def swim(self):
        print("hi")
    def speaks(self):
        print("bye")
class Dog:
    def swim(self):
        print("bye")
    def speaks(self):
        print("hi")

def display(duck):
    duck.swim() #it will call even dog fn
    duck.speaks()
    print("infor")
duck=Duck()
display(duck)
dog=Dog()
display(dog)

class Duck:
    def swim(self):
        print("hi")
    def speaks(self):
        print("bye")
class Dog:
    def swim(self):
        print("bye")
    def speaks(self):
        print("hi")

def display(obj):
    obj.swim() #it will call even dog fn
    obj.speaks()
    print("infor")
duck=Duck()
display(duck)
dog=Dog()
display(dog)"""

class Duck:
    def swim(self):
        print("Duck is swimming")
    
    def speaks(self):
        print("Duck says quack")

class Dog:
    def swim(self):
        print("Dog is swimming")
    
    def speaks(self):
        print("Dog says woof")

class Person:
    def speaks(self):
        print("Person says blah")

class Demo:
    def display(self, obj):
        obj.swim()
        obj.speaks()
        print("Additional information")

duck = Duck()
dog = Dog()
person = Person()

demo = Demo()
demo.display(duck)
demo.display(dog)

