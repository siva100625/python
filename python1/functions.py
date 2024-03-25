"""def greet():
    print("hi")
    print("hello")

greet()
greet()

def abc(a,b,c): #formal parameters or parameters
    print(a+b+c)
abc(1,2,3) #arguments or actual parameters
abc(7,8,9)

#positional arguments
def a(name,dept):
    print(f"hi {dept} i am {name}")
a("siva","ece")

def a(name,dept):
    print(f"hi {dept} i am {name}")
a("siva","ece")

#Keyword Arguments
def a(name,dept):
    print(f"hi {dept} i am {name}")
a(name="siva",dept="ece")

def a(name,dept):
    print(f"hi {dept} i am {name}")
a(dept="siva",name="ece")

#positional and keyword arg
def a(name,dept):
    print(f"hi {dept} i am {name}")
a("siva",dept="ece") # keyword argument should be after positional argument

#Default Arguments
def a(name,dept="cs"):
    print(f"{name} is {dept}")
a("siva")
 #name and subj are required argument
def a(name,subj,dept="cs"): # default argument should be last
    print(f"{name} is {dept} is {subj}")
a("siva","ggg","j")

#Arbritary arguments
#positional
def add(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
add(1,2,3,4,5)

# *args and **kwargs 

def add(*a,name):
    c=0
    for i in a:
        c=c+i
    print(c)
    print(name)
add(1,2,3,4,5,name="jenny")

def add(name,*a):
    c=0
    for i in a:
        c=c+i
    print(c)
    print(name)
add(1,2,3,4,5)

def info(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
info(name="Ram",age="30",dept="cse")
info(name="shyam",dept="cse")

def info(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    print(args)
info(1,2,name="Ram",age="30",dept="cse")
info(1,2,3,name="shyam",dept="cse")

def multiply(*args):
    c=1
    for i in args:
        c=c*i
    print(c)
multiply(2,3,-6,8)
multiply(2,5,8,9,1,6)"""

def add(a,b):
    c=a+b
    return c #explicit return

print(add(5,7))

def add(a,b):
    c=a+b
    return #implicit return
print(add(5,7))

def add(a,b): #implicit return
    c=a+b
print(add(5,7))

def name(f,l):
    c=f.title()
    d=l.title()
    return f"{c} {d}"
g=name("siva","subramanian")
print(g)

import statistics
def mmm(l):
    return statistics.mean(l),statistics.median(l),statistics.mode(l)

print(mmm([1,2,3,4,5,6]))#op is tuple

import statistics
def mmm(l):
    return [statistics.mean(l),statistics.median(l),statistics.mode(l)]
    print("h")# after the return no statement will be executed
print(mmm([1,2,3,4,5,6,1]))

#multiple return
def add(a, b):
    if a == 0 & b == 0:  # Corrected the logical operator from & to and
        return "no"
    else:
        return a + b

v = int(input("Enter first number: "))
v1 = int(input("Enter second number: "))
r = add(v, v1)  # Pass both numbers as arguments
print(r)
