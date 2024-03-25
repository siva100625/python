
#to do list
"""b=[]
def add(a):
    b.append(a)
def remove(d):
     b.pop(d-1)
def display():
     print(b)   
d=True
while d!=False:
     choice=int(input("enter the choice: 1 for add 2 for remove 3 for display "))
     if choice==1:
         a=input("enter the data:")
         add(a) 
         
     elif choice==2:
          c=int (input("enter the number you want to remove:"))
          remove(c)
     
     elif choice==3:
          display()
     else:
          d=False"""
#calculator
"""import os
def again(a,b,c):
    if c=='+':
        return a+b      
    elif c=='-':
        return a-b  
           
    elif c=='*':
        return a*b      
    elif c=='/':
        return a/b    
    else:
        print("invalid")
I=True
while I!=False:
    a=int(input("enter a number:"))
    print("+\n-\n*\n/")
    c=input("Pick an operation:")
    b=int(input("enter a second number:"))
    d=again(a,b,c)
    print(d)
    e=input(("enter y to continue with or n to new operation or exit:"))
    if e=='y':
     f=int(input("enter a number:"))
     j=input("Pick an operation:")
     e=again(d,f,j)
     print(e)
     e=input(("enter y to continue with or n to new operation or exit:"))
    elif e=='n':
         os.system('cls')
         continue
    else:
        I=False"""

#password generator
"""import random
import string
c=[]
a=0
b=int(input("enter how many numbers you want for your password?"))
for i in range(0,b):
    a=random.randint(1,9)
    c.append(a)
h=int(input("enter how many letter you want for your password?"))
for i in range(0,h):
    g=random.choice(string.ascii_letters)
    c.append(g)
l=int(input("enter how many symbols you want for your password?"))
for i in range(0,l):
    t=random.choice(string.punctuation)
    c.append(t)
random.shuffle(c)
#w="".join(map(str,c))
w=""
for i in c:
     w+=str(i)
print(w)"""

#rock paper scissors
"""i=True
score=0
while i!=False:
     a=int(input("Enter a number :(0 for rock\n1 for scissors\n2 for papers): "))
     import random
     b=random.randint(0,2)
     print(b)
     
     if a==0:
      print("user:👊🏻  ")
     elif a==1:
       print("user:✌🏻 ")
     else:
       print("user:️🤚🏻 ")
     if b==0:
      print("computer:👊🏻  ")
     elif b==1:
       print("computer:✌🏻  ")
     else:
            print("computer:️🤚🏻 ")
     if a==b:
       print("draw")
     elif a==0 and b==1:
       print("user wins")
       score+=1
     elif a==0 and b==2:
       print("computer wins")
     elif a==1 and b==0:
       print("computer wins")
     elif a==1 and b==2:
       print("user wins")
       score+=1
     elif a==2 and b==0:
            print("user wins")
            score+=1
     elif a==2 and b==1:
       print("computer wins")
     else:
            print("invalid number")
     i=int(input("do you want to continue 1 for yes or 0 for no:"))
print(score)
"""

#Contact book 
data=[]  
def add():
       name=input("enter your name:")
       email=input("enter the email:")
       address=input("enter your address:")
       phone=input("enter the phone no:")
       data.append({"name":name,"email":email,"address":address,"phone":phone})
def display():
     print(data)
def search():
      se=input("enter the name:")
      found=False
      for i in data:
            if se==i['name']:
                  True
                  found=True
                  break
            else:
               found=False
      if found==True:
            print(f"Contact information found:\nName: {i['name']}\nEmail: {i['email']}\nAddress: {i['address']}\nPhone:{i['phone']}")
      else:
            print("Contact Not Found")
def delete():
      print(data)
      print("which contact you wnat to delete:")
      a=int(input("enter the no:"))
      data.pop(a-1)
      print(data)
def update():
      print(data)
      a=int(input("enter the number to update:"))
      b=int(input("1 for name,2 for email,3 for address")) 
      if b==1:
            c=input("enter new name:")
            data[a-1]['name']=c
      elif b==2:
            f=input("enter new email:")
            data[a-1]['email']=f
      elif b==3:
            h=input("enter new address:")
            data[a-1]['address']=h
      elif b==4:
            y=input("enter new phone no:")
            data[a-1]['phone']=y            
       
            
b=True
while b!=False:
       print("enter the choice 1 for add contacts,2 for display,3 for search,4 for delete,5 for update")
       choice=int(input("enter the no:"))
       if choice==1:
            add()  
       elif choice==2:
            display() 
       elif choice==3:
            search() 
       elif choice==4:
             delete()
       elif choice==5:
             update()
       
       else:
            b=False

