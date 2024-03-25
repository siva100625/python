#exercise
"""a=(input("enter 2 digit no:"))
c=int(a[0])+int(a[1])
print(c)
"""
#CALCULATE BMI
"""w=int(input("in kg"))
h=float(input("in m"))
bmi=w/(h**2)
print(int(bmi))"""
#DAYS,WEEKS,MONTHS UNTILL 90 YEARS OLD
"""a=int(input("enter your age:"))
b=90-a
d=b*365
w=b*52
y=b*12
print(f"you have {d} days,{w} weeks,{y} months left")""" 
#odd or even
"""a=int(input("enter a number:"))
if a%2==0:
    print('even')
else:
    print('odd')"""
#updated BMI
"""w=int(input("in kg"))
h=float(input("in m"))
bmi=round(w/(h**2))
print(int(bmi))
if bmi<18.5:
    print("undeweight")
elif(bmi<25):
    print("normal weight")
elif(bmi<30):
    print("over weight")
elif(bmi<34.9):
    print("normal weight")
else:
    print("obese class 2")"""
"""#leap year or not
a=int(input("enter a year:"))
if a%4==0 and a%100!=0 or a%400==0:
    print("leap year")
else:
    print("not a leap year")"""
#pizza order program
"""print("Small Pizza=100\nMedium Pizza=200\nLarge Pizza=50")
a=input("Enter Your order")
if(a=='s'):
          t=100
          p=input("pepporoni for small pizza (y/n)")
          if(p=='y'):
                     t+=30
          o=input("need cream(y/n)")
          if(o=='y'):
                    t+=20
          print(f"bill is {t}")
elif(a=='m'):
            t=200
            p=input("pepporoni for medium pizza (y/n)")
            if(p=='y'):
                      t=200+50
            o=input("need cream(y/n)")
            if(o=='y'):
                      t+=20
            print(f"bill is {t}")
else:
            t=300
            p=input("pepporoni for large pizza (y/n)")
            if(p=='y'):
                      t=200+50
            o=input("need cream(y/n)")
            if(o=='y'):
                      t+=20
            print(f"bill is {t}")"""
#love calculator
"""a=input("enter your name:")
b=input("enter yout lover name:")
d=a+b.lower()
c=0
e=0
if d.count('t'):
    c+=1
if d.count('r'):
    c+=1
if d.count('u'):
    c+=1
if d.count('e'):
    c+=1
if d.count('l'):
    e+=1
if d.count('o'):
    e+=1
if d.count('v'):
    e+=1
if d.count('e'):
    e+=1
if d.count('e'):
    e+=1
l=str(c)+str(e)
f=int(l)
if f>90 and f<100:
                print(f"you will be a blast {f}%")
elif f>=50 and f<89:
                   print(f"you will be a okay {f}%")
else:
       print(f"your score {f}%")"""
#Heads or Tails
"""import random
a=random.randint(0,1)
if a==0:
    print(f"Tails:{a}")
else:
    print(f"Head:{a}")
"""
#Pay the bill
"""import random
a=['siva','lisa','rose','jenny']
print(a)
l=random.choice(a)
print(f"{l} will pay the bill")"""
"""import random
a=input("enter a string:")
c=a.count(" ")
c=c+1
t=a.split(" ")
print(t)
print(c)
r=random.randrange(0,c)
print(f"{t[r]} will pay the bill")"""
#hide the money
"""
f=[[1,1,1],[1,1,1],[1,1,1]]
a=int(input("enter two digit: "))
n=a
a=int(a%10)
n=int(n/10)
if(n>2 or a>2):  
              a=int(a%10)-1
              n=int(n/10)-1
              f[n][a]='X'
else:
     f[n][a]='X'

print(f"{f[0]}\n{f[1]}\n{f[2]}") 
"""
#average
"""
a=[]
c=0
n=int(input("enter a number:"))
for i in range(n):
    b=int(input("enter a number:"))
    c=c+b
    a.append(b)

print(a)
print(round(c/n))"""
#max
"""a=[]
n=int(input("enter the number:"))
for i in range(n):
    b=int(input("enter a number:"))
    a.append(b)
print(a)
max=a[0]

for i in a:
    if max<i:
        max=i
print(max)"""
#sum of even no
"""sum=0
for i in range(2,101,2):
    sum+=i
print(sum)

sum=0
for i in range(2,101):
    if(i%2==0):
           sum+=i
print(sum)"""

#fizzbuzz 
"""for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#Paint the wall
import math
def paint(a,b,c):
    can=a*b/c
    print(math.ceil(can))

a=int(input("enter the width:"))
b=int(input("enter the height:"))
c=int(input("enter the coverage:"))
paint(a=a,b=b,c=c)
    
#prime number or not
import math
def prime(a):
    if a==1 or a==2 or a==3:
         flag=0
         return flag

    for i in range(2,math.ceil(a/2)+1):
        flag=0
        if a%i==0:
            flag=1
            break
            
        return flag
        

a=int(input("enter a number:"))
o=prime(a)
if o==0:
        print(f"The given Number is Prime {a}")
else:
    print(f"The given number is not prime {a}")    
#another method
import math

def prime(a):
    if a == 1:
        return False  # 1 is not a prime number
    
    for i in range(2, math.isqrt(a) + 1):
        if a % i == 0:
            return False  # Found a factor, so it's not prime
    return True  # No factors found, so it's prime

a = int(input("Enter a number: "))
is_prime = prime(a)
if is_prime:
    print(f"The given number {a} is prime.")
else:
    print(f"The given number {a} is not prime.")
#dict
student_marks={
    "jenny":92,
    "harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Ankiet":99,
    "Prem":34
}
new=student_marks
for i in student_marks:
    if student_marks[i]>90:
        new[i]='A+'
    elif student_marks[i]>80:
        new[i]='A'
    elif student_marks[i]>70:
        new[i]='B+'
    elif student_marks[i]>60:
        new[i]='B'
    elif student_marks[i]>50:
        new[i]='C'
    elif student_marks[i]>40:
        new[i]='D'
    else:
        new[i]='F'
print(new)

#nested
def nest(name,age,course):
    travel_data.append({
    "name":name,
    "age":age,
     "course":course,
})
   


travel_data = [
    {
        "Ram": 2,
        "roll_no": 10,
        "age": 20,
        "course": "python"
    },
    {
        "Ra": 9,
        "roll_no": 100,
        "age": 920,
        "course": "pytn",
        "phone": [123, 44]
    }
]
nest(name="siva",age="18",course="python")
print(travel_data)

def check(a,b):
    if a=='' and b=='':
        return "enter valid input"
    else:
        return a,b
    
c=input("enter a fn")
d=input("enter a ln")
f=c.title()
l=d.title()
n=check(f,l)
print(n)

def month (a,b):
    if a=='january':
        return 31
    elif a=='february' and (b%4==0 and b%100!=0 or b%400==0):
        return 28
    elif a=='february':
        return 29
    elif a=='march':
        return 31
    elif a=='april':
        return 30
    elif a=='may':
        return 31
    elif a=='june':
        return 30
    elif a=='july':
        return 31
    elif a=='august':
        return 31
    elif a=='september':
        return 30
    elif a=='october':
        return 31
    elif a=='november':
        return 30
    elif a=='december':
        return 31
    
a=(input("enter a month:"))
b=int(input("enter a year:"))
c=month(a,b)
print(c)"""
