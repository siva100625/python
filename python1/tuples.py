t=(1,2,3,True,"str",3,1.1)
print(type(t),t,t[2])
t=(10)
print(type(t))
t=(10,)
print(type(t))#because of the unchangeble behaviour inc the speed of the program
i=(1,2,3,4,5)
print(i[1:4])
print(i[::2])
print(len(i))
r=(t,i)
print(r,r[1],len(r))
f=t+i
print(f,len(f))
print(min(i),max(i),i.count(1),i.index(1))
l=[1,2,3,4]
print(tuple(l))
print(list(i))
o=(10,'j')*5
print(o)
p=(l,i)
print(p)

