t1 = (1,2,3,4,5)
t2=(7,8,9,4,5)
#+
print(t1+t2)
#*
print(t1*3)
#membership
1 in t1
#iteration
for i in t1 :
  print(i)



t=(1,2,3,4,5)
print(len(t))

print(sum(t))

print(min(t))

print(max(t))

print(sorted(t))

print(sorted(t,reverse=True))


#count

print(t.count(5))


print(t.index(2))

#tuple unpacking

a,b,c =(1,2,3)
print(a,b,c)

a=1
b=2
a,b=b,a

print(a,b)

a,b,*others =(1,2,3)
print(a,b)
print(others)

#zip func

a=(1,2,3,4)
b=(7,8,9,4)

print(tuple(zip(a,b)))