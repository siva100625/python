from typing import Any


list=[1,0,-1]
print(len(list))
print(list)
print(type(list))
class Demo:
    name="jenny"
d=Demo()
print(d)
class Author:
    def __init__(self, n, b):
        self.name = n
        self.b = b

    def __len__(self):
        return self.b

    def __str__(self):
        return f"{self.name} {self.b}"

    def __call__(self, *args, **kwargs):
        print("hi")

    def __del__(self):
        print("BYye")

d = Author("s", 22)
print(d)   # Output: s 22
print(len(d))  # Output: 22
d()  # Output: hi
del d  # Output: BYye
print(dir(int))
