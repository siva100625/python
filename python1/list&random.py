"""mix=[1,'to',True,1.1,1]
m=[6,3,2,8,9]
print(mix)
print(mix[3])
print(mix[-1])
print(len(mix))
print(mix[0:4])
print(mix[0:])
print(mix[:])
print(mix[0:3])
print(mix[:3])
print(mix[0:5:2])
m.sort()
print(m)
m.reverse()
print(m)
print(max(m))
print(min(m))
m.append(35)
print(m)
m.insert(2,6)
print(m)
m.extend([36,89,90,0])
print(m)
m[3]=7
print(m)
m[1:4]=[7,4,1]
print(m)
m.remove(0)
print(m)
print(m.pop())# but in remove it wont return
print(m)
m.pop(0)#index
print(m)
m.count(1)
print(m)#no output
print(m.count(1))
m.clear()
print(m)
# Create a list
a = [1, 2, 3, 4, 5]

# Demonstrate the copy() method
b = a.copy()

# Print both lists
print("Original list:", a)
print("Copied list:", b)

# Modify the copied list
b[0] = 10

# Print both lists again to show the difference
print("After modification:")
print("Original list:", a)
print("Modified list:", b)

# Demonstrate the index() method
element = 3
index = a.index(element)

# Print the index of the element
print(f"The index of {element} in the original list is:", index)
# Create a list
a = [1, 2, 3, 4, 5, 3, 6, 7, 8]

# Demonstrate the index() method with optional start and end parameters
element = 3
start_index = 2
end_index = 7
index = a.index(element, start_index, end_index)

# Print the index of the element within the specified range
print(f"The index of {element} between index {start_index} and {end_index} is:", index)

"""
"""
import random
a=random.randint(1,3)
b=random.randrange(1,3)
c=random.random()
print(a,b,c)
d=random.uniform(1,3)
print(d)
l=[1,2,3,4,5,6]
e=random.choice(l)
print(e)
r=[3,5,2,7,8,0]
random.shuffle(r)
print(r)
"""
n=[1,2,3,[34,55,77],8,9]
print(len(n)-2)
print(n[3])
print(n[3][0])
print(n[3][0:2])
print(n[3][::2])
l1=[1,2,3,["si","f","ly"],7]
print(len(l1))
print(l1[3][2])

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
c = 0  # Initialize the counter

for row in grid:
    for num in row:
        if num < 0:
            c += 1

print(c)  # Output the count of negative numbers
