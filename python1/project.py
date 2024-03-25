"""a=int(input("Enter a number :(0 for rock\n1 for scissors\n2 for papers): "))
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
elif a==0 and b==2:
       print("computer wins")
elif a==1 and b==0:
       print("computer wins")
elif a==1 and b==2:
       print("user wins")
elif a==2 and b==0:
       print("user wins")
elif a==2 and b==1:
       print("computer wins")
else:
       print("invalid number")"""
#Password Generator
"""
import random
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

#Hangman game

"""import random

a = ['apple', 'banana', 'grapes', 'lava']
b = random.choice(a)
print(b)
c = len(b)
o = ['-'] * c  # Initialize list with dashes representing unguessed letters
print(o)

print("Guess the word")

u = 6
gameover = False

while not gameover:
    d = input("Enter a letter: ")
    found = False  # Flag to indicate if the guessed letter is found in the word

    for i in range(c):
        if b[i] == d:
            o[i] = d
            found = True

    if not found:
        u -= 1
        print(f"Incorrect guess. You have {u} guesses left.")

    print(o)

    if '-' not in o:
        gameover = True
        print("Congratulations! You guessed the word:", b)
    elif u == 0:
        gameover = True
        print("Game over! The word was:", b)
"""

#Ceaser Cipher

#plain to cipher encryption
#cipher to plain decryption
"""def encrypt(a):
              print("Type your message:")
              b=input()
              print("type the shift number:")
              c=int(input())
              d=len(b)
              f="abcdefghijklmnopqrstuvwxyz"
              p=""
              for i in range(0,d):
                    for j in range(0,26):
                         if b[i]==f[j]:
                              p+=f[j+c]
              return p

def decrypt(v):
              print("type the shift number:")
              c=int(input())
              d=len(b)
              f="abcdefghijklmnopqrstuvwxyz"
              p=""
              for i in range(0,d+1):
                    for j in range(0,26):
                         if v[i]==f[j]:
                              p+=f[j-c]
              return p
             
print("Type 'encrypt' for encryption, type 'decrypt' for decryption:")  
end=True
while end==False:
              a=input()
              if a=='encrypt':
                             v=encrypt(a)
                             print(v)
              print("Type yes to go again otherwise no")
              b=input()
              if b=='yes':
                      print("Type 'encrypt' for encryption, type 'decrypt' for decryption:")  
                      s=decrypt(v)
                      print(s)
              if b=='no':
                      end=True
                      print("bye")
    
    
print("Type your message:")
b = input()
print("Type the shift number:")
c = int(input())

d = len(b)
f = "abcdefghijklmnopqrstuvwxyz"
result_encryption = ""
result_decryption = ""

# Encryption
for i in range(d):
    char = b[i]
    if char.isalpha():
        if char.islower():
            result_encryption += f[(f.index(char) + c) % 26]
        else:
            result_encryption += f[(f.index(char.lower()) + c) % 26].upper()
    else:
        result_encryption += char

# Decryption
for i in range(d):
    char = result_encryption[i]
    if char.isalpha():
        if char.islower():
            result_decryption += f[(f.index(char) - c) % 26]
        else:
            result_decryption += f[(f.index(char.lower()) - c) % 26].upper()
    else:
        result_decryption += char

print("Encrypted message:", result_encryption)
print("Decrypted message:", result_decryption)


#Silent Auction program
import os
def final(c):
    d = 0
    winner = ""
    for i in c:
        price = c[i]
        if price > d:
            d = price
            winner = i
    print(c)
    print(f"The winner is {winner} with a bid price of {d}")

y = True
c = {}
while y:
   
        name = input("What's your name:")
        bid = int(input("What's your bid:"))
        c[name] = bid
        a = input("Enter the auction for yes otherwise no:").lower()
        if a == 'no':
             y = False
             final(c)
        elif a=='yes':
             os.system('cls')
             
#advanced
 calculator

import os

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
        I=False

#Random 

def check(a,c):
        if c>a:
                print("high")
        else:
                print("low")
        

import random
import logo
g=False
while g!=True:
            a=random.randint(1,50)
            print(logo.logo)
            b=(input("easy or hard:"))
            if b=="easy":
                    i=10
                    while i>0:
                            i=i-1
                            c=int(input("enter the no:"))
                            if c==a:
                                  print("no is found")
                                  break
                            else:
                                check(a,c)  
                                print(f"you have {i} guesses left") 
                    else:
                           g=True           
            if b=="hard":
                    i=5
                    while i>0:
                            i=i-1
                            c=int(input("enter the no:"))
                            if c==a:
                                  print("no is found")
                                  break
                            else:
                                check(a,c)  
                                print(f"you have {i} guesses left") 
            
                    else:
                           g=True

#higher lower game
import random
import database
import logo
import os
d=True

while d!=False:
                print(logo.l1)
                a=random.choice(database.data)
                print(f"Compare 1:{a['name']} , {a['description']} , {a['country']}")
                print(logo.l2)
                b=random.choice(database.data)
                print(f"Compare 2:{b['name']} , {b['description']} , {b['country']}")
                g=input("highest follower one or two:").lower()
                point=0
                if g=="one":
                        
                        if a['follower']>b['follower']:
                                                    point+=1      
                                                    print(f"you scored {point}")      
                        else:
                                print("you lose")
                                os.system('cls')
                                print(f"you scored {point}") 
                                print(logo.l1) 
                                d=False
                elif g=="two":
                        if b['follower']>a['follower']:
                                                    point+=1 
                                                    print(f"you scored {point}")        
                        else:
                                print("you lose")  
                                os.system('cls') 
                                print(logo.l1)
                                print(f"you scored {point}")  
                                d=False      
                else:
                        print("invalid input")

#Coffee Machine Project
def check(order):
      for i in order:
            if order[i]>resources[i]:
                  print(f"not enough {i}")
                  return False
      return True
def coins():
      print("insert coin")
      t=0
      a=5*int(input("5Rs:"))
      b=10*int(input("10Rs:"))
      c=20*int(input("20Rs:"))
      t=a+b+c
      return t
def suc(a,b):
      if a>=b:
            global profit
            profit+=b
            c=a-b
            print(f"Here is your Rs{c} in change")
            return True
      else:
            print("Sorry thats not enough money. money refunded")
            return False
def make(a,order):
      for i in order:
           resources[i]-=order[i]
      print(f" enjoy your {a}")   

profit=0
menu={
      "latte":{
            "ingredients":{
                   "water":200,
                   "milk":150,
                   "coffee":24,
            },
            "cost":150
      },
      "cappuccino":{
            "ingredients":{
                   "water":250,
                   "milk":100,
                   "coffee":24,
            },
            "cost":200
      },
      "expresso":{
            "ingredients":{
                   "water":50,
                   "coffee":18,
            },
            "cost":100
      }
}
resources={
      "water":500,
      "milk":200,
      "coffee":100,
}
is_on=True
while is_on:
      choice=input("what would you like to have?(latte/expresso/cappuchino)")
      if choice=="off":
            is_on=False
      if choice=="report":
            print(f"Water={resources['water']}ml")
            print(f"Milk={resources['milk']}ml")
            print(f"coffee={resources['coffee']}ml")
            print(f"money=Rs{profit}")
      else:
            coffe_type=menu[choice]
            print(coffe_type)
            if check(coffe_type["ingredients"]):
                 pay=coins()      
                 if suc(pay,coffe_type['cost']):
                       make(choice,coffe_type['ingredients'])"""

#to do list
b=[]
def add(a):
    b.append(a)
def remove(d):
     b.pop(d-1)
def display():
     print(b)   
d=True
while d!=False:
     choice=int(input("enter the choice: "))
     if choice==1:
         a=input("enter the data:")
         add(a) 
         
     elif choice==2:
          c=int (input("enter the number you want to remove:"))
          remove(c)
     
     elif choice==3:
          display()
     else:
          d=False
