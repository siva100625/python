"""a=1
print(type(a))

print(type("hello"))

def display():
    pass
print(type(display))

def display():
    pass
print("Hello".lower())
"""
#how to define a class
"""
class Instructor: #class is a user defined datatype 
                 pass
instructor1=Instructor() 
print(type(instructor1))

class CarDesign:
        pass
lamborghini=CarDesign()
ferrari=CarDesign()
print(type(lamborghini))
print(type(ferrari))"""
"""
#Self and init 
class North:
    def __init__(self):
        print("newobj")

Lights=North() #self=Lights
Lights.color="red"
Lights.place="Alaska"
print(Lights.color)

Lights1=North() #self=Lights1
Lights1.color="blue"
Lights1.place="Finland"
print(Lights1.color)
"""
class North:
    def __init__(self,color,place):
        self.color=color
        self.place=place

Lights=North("jenny","Alaska") #self=Lights
print(Lights.color)

Lights1=North("SIva","tuty") #self=Lights1 
print(Lights1.color)

Lights1=North("b","k") #self=Lights1
print(Lights1.color)
"""
class North:
    def __init__(self,color,place):
        self.c=color
        self.p=place

Lights=North("jenny","Alaska")
print(Lights.c)

Lights1=North("SIva","tuty") 
print(Lights1.p)

class North:
    def __init__(self,c,p): 
        self.color=c
        self.place=p

Lights=North("jenny","Alaska")#u need to pass exactly 2 arguments otherwise error
print(Lights.color)

Lights1=North("SIva","tuty") 
print(Lights1.color)

class North:
    def __init__(self,c,p,f): 
        self.color=c
        self.place=p
        self.follow=f

Lights=North("jenny","Alaska",0)#u need to pass exactly 2 arguments otherwise error
print(Lights.color)
print(Lights.follow)
Lights1=North("SIva","tuty",0) 
print(Lights1.color)
print(Lights1.follow)


class North:
    def __init__(self,c,p): 
        self.color=c
        self.place=p
        self.followers=0

Lights=North("jenny","Alaska")#u need to pass exactly 2 arguments otherwise error
print(Lights.color)
print(Lights.followers)

Lights1=North("SIva","tuty") 
print(Lights1.color)
print(Lights1.followers)

class North:
    def __init__(self,c,p): 
        self.color=c
        self.place=p
        self.followers=0

Lights=North("jenny","Alaska")#u need to pass exactly 2 arguments otherwise error
print(Lights.color)
print(Lights.followers)

Lights1=North("SIva","tuty") 
print(Lights1.color)
print(Lights1.followers)

Lights2=North("di","dam")
print(Lights2.color)
print(Lights2.place)

Light3=North("k","l")
print(Light3.color)
print(Light3.place)


class Instructor:
    followers=0 #class obj var
    def __init__(self,name,address):
        self.name=name
        self.address=address

    
Instructor_1=Instructor("jenny","mumbai")
print(Instructor_1.name)
Instructor_2=Instructor("Jiya","gujarath")
print(Instructor_2.followers)"""
#methods
"""class Instructor:
    followers=0 #class obj var
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):# this self will bind/recieve the object
        print("hi")
        
        
Instructor_1=Instructor("jenny","mumbai")
print(Instructor_1.name)
Instructor_2=Instructor("Jiya","gujarath")
print(Instructor_2.display())

class Instructor:
    followers=0 #class obj var
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def display(self):# this self will bind/recieve the object
        print(f"hi I am {Instructor_1.name}")
        
Instructor_1=Instructor("jenny","mumbai")
print(Instructor_1.name)
Instructor_1.display()

class Instructor:
    followers=0 #class obj var
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def display(self):# this self will bind/recieve the object
        print(f"hi I am {self.name}") #because self=Instuctor_1
        
Instructor_1=Instructor("jenny","mumbai")
print(Instructor_1.name)
Instructor_1.display()

class Instructor:
    followers=0 #class obj var
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def display(self,sub):# this self will bind/recieve the object
        print(f"hi I am {self.name} I teach {sub}") #because self=Instuctor_1
        
Instructor_1=Instructor("jenny","mumbai")
print(Instructor_1.name)
Instructor_1.display("python")

class Instructor:
    followers=0 #class obj var but you can access it by obj name
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def display(self,sub):# this self will bind/recieve the object
        print(f"hi I am {self.name} I teach {sub}") #because self=Instuctor_1
    def update(self):
        self.followers+=1

Instructor_1=Instructor("jenny","mumbai")
Instructor_2=Instructor("jenny","mumbai")
print(Instructor_1.name)
Instructor_1.display("python")
Instructor_1.update()
print(Instructor_1.followers)
print(Instructor_2.followers)
Instructor_2.update()
print(Instructor_2.followers)
"""











