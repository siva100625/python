#method overloading-compile time polymorphism,within the same class,same name diff para same loc
"""class Demo:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
d=Demo()
#print(d.add(2,3))# method overloading
print(d.add(1,2,3))

class Demo:
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c):
        return a+b+c
d=Demo()
d.add(2,3,8)# method overloading
print(d.add(1,2,3))

class Demo:
    def add(self,a,b,c=0):
        return a+b+c

d=Demo()
print(d.add(2,3))# method overloading

class Demo:
    def add(self,*args):
       t=0
       for i in args:
           t=t+i
       return t

d=Demo()
print(d.add(2,3))
print(d.add(1,2,3))"""

#method overriding-runtime polymorphism,in inheritance,same name same para diff loc
class Father:
    def sleep(self):
        print("hi")
    def eat(sleep):
        print("eat")
class Son(Father):
    def sleep(self):
        print("llll")
Ram=Son()
Ram.sleep()

class Father:
    def sleep(self):
        print("hi")
    def eat(sleep):
        print("eat")
class Son(Father):
    def sleep(self):
        print("llll")
        super().sleep()
Ram=Son()
Ram.sleep()
