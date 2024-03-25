"""l = ['sica', 'cava', 'mava']
s = ['hi', 'hello', 'welcome']

for i in l:
    for j in s:
        print(i, j)
        if j == "hello" and i == "cava":
            break
    print("out from inner loop")

print("out from outer loop")
"""
"""l = ['sica', 'cava', 'mava']
s = ['hi', 'hello', 'welcome']

for i in l:
    for j in s:
        if j == "hello" and i == "cava":
            continue
        else:
            print(i, j)
    print("out from inner loop")

print("out from outer loop")
c = 1
while c <= 10:
    if c == 8:
        c += 1  # Increment c here to avoid infinite loop
        continue
    else:
        print(c)
        c += 1  # Increment c for each iteration
for i in range(1,11):
    if i==7:
        continue
    else:
        print(i)"""

for i in range(1,11):
    pass   #used for future purposes

