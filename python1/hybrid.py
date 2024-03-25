"""class A:
    def display(self):
        print("hi")

class B(A):
    def display(self):
        print("hello") #single inheritance
class C:
    def show(self):
        print("Hola")

class D(B,C): #multiple inheritance
     def display(self):
         print("Bye")

d1=D()
d1.display()
print(f"D.mro() first D ,B,A,C")

class University:
    cname="sri eshwar"
    def show(self):
        print(f"name:{self.cname}")

class Branch(University):
        na="BE"
        def show(self):
           print(f"name:{self.na}")


class Course(University):
      n="Ece"
      def show(self):
        print(f"name:{self.n}")

class Student(Course,Branch):
     name="siva"
     def show(self):
        print(f"name:{self.name} Course:{self.n} Branch:{self.na} college:{self.cname}")

class Faculty(Branch):
    name="jenny"
    def show(self):
        print(f"name:{self.name}  Branch:{self.na} college:{self.cname}")

u=University()
u.show()
b=Branch()
b.show()
c=Course()
c.show()
s=Student()
s.show()
f=Faculty()
f.show()

#Diamond Problem

class A:
    def display(self):
        print("hi")

class B(A):
    def display(self): #left to reight then deep
        print("hello") #single inheritance
class C(A):
    def display(self):
        print("Hola")

class D(B,C): #multiple inheritance
     pass
d1=D()
d1.display()
print(D.mro())

class A:
    def display(self):
        print("hi")

class B(A):
       pass

class C(A):
    def display(self): #left to reight then deep
        print("Hola")

class D(B,C): #multiple inheritance
     pass
d1=D()
d1.display()
print(D.__mro__)

class A:
    def display(self):
        print("hi")

class B(A):
       pass

class C(A):
    pass

class D(B,C): #multiple inheritance
     pass
d1=D()
d1.display()   #left to reight then deep
print(D.__mro__)"""




























































































