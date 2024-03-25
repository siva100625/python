"""print(dir())
print(__name__)

print("hi")
def display(name):
    return name
def do():
    print("lll")


name=input("enter")
print(display(name))


def display(name):
    return name
def do():
    print("lll")

if __name__=="__main__":
            print("first")
            name=input("enter")
            print(display(name))"""

def display(name):
    return name
def do():
    print("lll")

if __name__=="__main__":
            print("first")
            name=input("enter")
            print(display(name))
do()

def display(name):
    return name
def do():
    print("lll")

if __name__=="__main__": #to prevent the part of code even when the modules are importes
            print("first")
            name=input("enter")
            print(display(name))
            do()
