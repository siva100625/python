"""i=1
while i<5:
    print("hi")
    i=i+1
while i<5:print("hi");i=i+1
while i<5:
    print("hi")
    i=i+1
else:
    print("sucess")
while i<5:
    print("hi")
    i=i+1
    if i==2:
        break
else:
    print("sucess")

#sentinel number
n=int(input("enter a number(-1 to quit)"))
while n!=-1:
    print(n)
    n=int(input("enter a number(-1 to quit)"))
else:
    print("else block")

count=0
while True:
    print(count)
    count+=1
    if count==5:
        break
else:
     print("in else block") """
u=int(input("enter a number(0 to quit):"))
sum=0
while u!=0:
    sum+=u
    u=int(input("enter a number(0 to quit):"))
print(sum)
