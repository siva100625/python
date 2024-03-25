"""class Human: #object class:parent of all class
    def eat(self):
        print("eat")
    def ji(self):
          print("walking")
class Male(Human):
        def sleep(self):
           print("sleep")
class Boy(Male):
     def ji(self):
          Human.ji(self)
          super().ji()
          print("walk")

class p(Boy):
     pass
boy_1=Boy()
boy_1.eat()
boy_1.ji()
h=p()
h.ji()


class Human: #object class:parent of all class
    def __init__(self,n):
         self.n=n
         self.a=2
         print("uuuu")
    def eat(self):
        print("eat")
    def ji(self):
          print("walking")
class Male(Human):
        def sleep(self):
           print("sleep")
class Boy(Male):
  
     def ji(self):
          Human.ji(self)
          super().ji()
          print("walk")

boy_1=Boy("k")
boy_1.eat()
print(boy_1.n)
print(boy_1.a)
print(Boy.mro())

class Human: #object class:parent of all class
    def __init__(self,n):
         self.n=n
         self.a=2
    def eat(self):
        print("eat")
    def ji(self):
          print("walking")
class Male(Human):
        def __init__(self,name):
             self.name=name
             print("yyyy")
        def sleep(self):
           print("sleep")
class Boy(Male):
  
     def ji(self):
          Human.ji(self)
          super().ji()
          print("walk")

boy_1=Boy("k")
boy_1.eat()
print(boy_1.name)
print(Boy.mro())"""

class Human: #object class:parent of all class
    def __init__(self,n):
         self.n=n
         self.a=2
    def eat(self):
        print("eat")
    def ji(self):
          print("walking")
class Male(Human):
        def __init__(self,name):
             self.name=name
             print("yyyy")
        def sleep(self):
           print("sleep")
class Boy(Male):
      def __init__(self, name,k,n):
           Human.__init__(self,n)
           Male.__init__(self,k)
           self.name=name
      def ji(self):
          Human.ji(self)
          super().ji()
          print("walk")

boy_1=Boy("p","k","l")
boy_1.eat()
print(boy_1.name)
print(boy_1.n)
print(boy_1.name)

class Human: #object class:parent of all class
    def __init__(self,n):
         self.n=n
         self.a=2
    def eat(self):
        print("eat")
    def ji(self):
          print("walking")
class Male(Human):
        def __init__(self,name):
             self.na=name
             print("yyyy")
        def sleep(self):
           print("sleep")
class Boy(Male):
      def __init__(self, name,k,n):
           Human.__init__(self,n)
           Male.__init__(self,k)
           self.name=name
      def ji(self):
          Human.ji(self)
          super().ji()
          print("walk")

boy_1=Boy("p","k","l")
boy_1.eat()
print(boy_1.name)
print(boy_1.n)
print(boy_1.na)

class Human: 
    cl=0#object class varialble
    def __init__(self,n):
         self.n=n
         self.a=2
    def eat(self):
        print("eat")
    def ji(self):
          print("walking")
class Male(Human):
        def __init__(self,name):
             self.na=name
             print("yyyy")
        def sleep(self):
           print("sleep")
class Boy(Male):
      def __init__(self, name,k,n):
           Human.__init__(self,n)
           Male.__init__(self,k)
           self.name=name
      def ji(self):
          Human.ji(self)
          super().ji()
          print("walk")

boy_1=Boy("p","k","l")
boy_1.eat()
print(boy_1.name)
print(boy_1.n)
print(boy_1.na)
print(boy_1.cl)
