"""if 5>6:
    print('g')
else:
    print('j')"""
"""if(5>6):
    print('g') #indentation error wiil happen be careful
else:
    print('j')"""
"""if(5==5):
    print('g')
print("k")"""
"""if 5>6:
    print('g')
    if 5>6:
          print('g')
    else:
         print('j')
else:
    print('j')"""
"""if 5<6:
    print('g')
    if 5>6:
          print('g')
    elif 5<6:
            print('jll')
else:
    print('j')"""
n=int(input("enter a number:"))
if n%2==0:
    if n>2 and n<5:
         print("Not Weird")
    if n>6 and n<20:
         print("Weird")
    if n>20:
         print("Not Weird")
    
else:
    print("odd")


