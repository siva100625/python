"""class Human:
    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
    pass
boy_1=Boy()
boy_1.sleep()
boy_1.eat()
boy_1.work()

class Human:
    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Male,Human):#when you have same method name in both parent class first name matters
    pass
boy_1=Boy()
boy_1.sleep()
boy_1.eat()
boy_1.work()

class Human:
    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
    pass
boy_1=Boy()
boy_1.sleep()
boy_1.eat()
boy_1.work()
Male.work(boy_1)

class Human:
    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def go(self):
         print("hi")
     def work(self):
         print("I an m") 
   
boy_1=Boy()
boy_1.sleep()
boy_1.eat()
Human.work(boy_1)
Male.work(boy_1)
boy_1.work() #first own fn next parent cls method
print(Boy.mro())#mro=method resolution order 


class Human:
    def eat(self):
        print('I can eat')
  

class Male:
    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def go(self):
         print("hi")
   
   
boy_1=Boy()
boy_1.sleep()
boy_1.eat()
boy_1.work() #first own fn next parent cls method
print(Boy.mro())#mro=method resolution order 

class Human:
    def __init__(self):
        self.e=2
        self.m=4

    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def __init__(self,name):
        self.name=name

    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def go(self):
         print("hi")
     def work(self):
         print("I an m") 
   
boy_1=Boy()
print(boy_1.e)
print(boy_1.m)

class Human:
    def __init__(self):
        self.e=2
        self.m=4
        print("base")

    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def __init__(self,name):
        self.name=name
        print("2")

    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def __init__(self,name):
         Male.__init__(self,name)
         
     def go(self):
         print("hi")
     def work(self):
         print("I an m") 
   
boy_1=Boy("siva")#you cant acess human class

class Human:
    def __init__(self):
        self.e=6
        self.m=4
        print("base")

    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def __init__(self,name):
        self.name=name
        print("2")

    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def __init__(self,name):
         Male.__init__(self,name)
         Human.__init__(self)
         
     def go(self):
         print("hi")
     def work(self):
         print("I an m") 
   
boy_1=Boy("siva")
print(boy_1.e)

class Human:
    def __init__(self,n):
        self.e=6
        self.n=n
        print("base")

    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def __init__(self,name):
        self.name=name
        print("2")

    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def __init__(self,name):
         Male.__init__(self,name)
         Human.__init__(self,9)
         
     def go(self):
         print("hi")
     def work(self):
         print("I an m") 
   
boy_1=Boy("siva")
print(boy_1.n)
"""
class Human:
    def __init__(self,n,m):
        self.e=6
        self.n=n
        self.m=m
        print("base")

    def eat(self):
        print('I can eat')
    def work(self):
        print("I code")

class Male:
    def __init__(self,name):
        self.name=name
        print("2")

    def sleep(self):
        print("i can Sleep")
    def work(self):
        print("code")

class Boy(Human,Male):#when you have same method name in both parent class first name matters
     def __init__(self,name,n,m,k):
         Male.__init__(self,name)
         Human.__init__(self,n,m)
         self.k=k
         
     def go(self):
         print("hi")
     def work(self):
         print("I an m") 
     def display(self,m,n):
         print(f"Hi i am {m} and i work at {n}")
     def display1(self):
         print(f"Hi i am {self.name} and i work at {self.n}")
   
boy_1=Boy("siva","py",7,"l")
print(boy_1.m)
print(boy_1.n)
print(boy_1.k)
boy_1.display("siva","py")
boy_1.display1()



