"""import os

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def calculator():
    a = int(input("Enter a number: "))
    operation = input("Pick an operation (+, -, *, /): ")
    b = int(input("Enter a second number: "))
    result = operations[operation](a, b)
    print("Result:", result)

    choice = input("Enter 'y' to continue, 'n' for a new operation, or any other key to exit: ")
    if choice.lower() == 'y':
        calculator()
    elif choice.lower() == 'n':
        os.system('cls')  # For clearing the screen on Windows. Use 'clear' on Unix-like systems.
        calculator()  # Recursive call for a new operation
    else:
        return

calculator()  # Start the calculator"""


#local global scope

a=10
def display():
    a=15
    print(a)
display()

a=10
def display():
    print(a)
display()

a=10
def display():
    a=15
display()
print(a)

a=10
def display():
    a=15
    def show():
        print(a)
display()

a=10
def display():
    def show():
        print(a)
display()

#global keyword

a=10
def display():
    global a
    a=a+1
    print(a)
display()

def display():
    a=15
    def show():
        global a # should be outside of all function this is error
        a=a+1
        print(a)
    show()
display()

def display():
    a=20
    def show():
        global a #creating a global variable
        a=30
    print(f"value before {a}")
    show()
    print(f"value after {a}")
display()
print(a)

name="jenny"
def display():
    global name
    name=name+"lectures"
print(name)
display()
print(name)



