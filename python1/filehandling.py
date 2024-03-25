#create
#f=open("file_1.txt","x") 

#read
"""f=open("file_1.txt","r")
data=f.read()
print(data)

#default
f1=open("file_1.txt")
data=f.read()
print(data)

#write if the file doesnt exist
f2=open("file_2.txt","w")
f2.write("welcome to jennys lectures")

#write if the file exist

f2=open("file_2.txt","w")
f2.write("welcome to Khatri lectures")

#r+ first read then write

f1=open("file_1.txt","r+")
print(f1.read())
f1.write("Python")

#w+ first write then read

f1=open("file_1.txt","r+")
f1.write("Python")
print(f1.read())

#tell

f1=open("file_1.txt","r+")
print(f1.tell())
f1.write("Python")
print(f1.tell())
print(f1.read())
print(f1.read())

#w+ if the file doesnt exist

f1=open("file_3.txt","w+")
print(f1.tell())
f1.write("Python")
print(f1.tell())
print(f1.read())
print(f1.read())
f1.close()

#w+ if the file exist

f1=open("file_1.txt","w+")
print(f1.tell())
f1.write("Python")
print(f1.tell())
print(f1.read())
print(f1.tell())
print(f1.read())
print(f1.tell())
f1.close()

#seek

f1=open("file_1.txt","w+")
print(f1.tell())
f1.write("Python")
print(f1.tell())
f1.write(" ffffffff")
f1.seek(0)
print(f1.read())
print(f1.tell())
f1.write("llllllllll")
print(f1.read())
print(f1.tell())
f1.close()

#append if the file exist

f1=open("file_1.txt","a")
f1.write("Hello")

#append if the file doesnt exist

f1=open("file_4.txt","a")
f1.write("Hello")

#append+ if the file exist

f1=open("file_1.txt","a+") #if the file is not in your current directory give the full path name
print(f1.tell())
print(f1.read())
f1.write("Hello")
print(f1.tell())
print(f1.read())
f1.seek(0)
print(f1.read())

#image

f1=open("image.jpg","rb") #if the file is not in your current directory give the full path name
print(f1.read())


f1=open("image.jpg","wb+")
f2=open("image2.avif","rb") #if the file is not in your current directory give the full path name
for i in f2:
    f1.write(i)
print(f1.read())"""














