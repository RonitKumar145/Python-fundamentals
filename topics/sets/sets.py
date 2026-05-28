#empty
s=set()
print(s)
print(type(s))
#1d set
s1 ={1,2,3}
print(s1)

#2d set not allowed

#sets are unodered position decided by hashing
s2={1,'hello',4.5,True,(1,2,3,)}
print(s2)

#type conversion

s3= set([1,2,3])
print(s3)

s4 ={1,2,3,4,5}
print(s4)


s10={1,2,3}
s11={3,2,1}

print(s10==s11) #true since sets are unorderd


#accessing not possible since they are unorderd 


#editing also not possible 


#adding and deletion possible 

s5={1,2,3}
s5.add(5)
print(s5)

s5.update([6,7,8,9,10])
print(s5)



print(s)
del s
#print(s)

s5.discard(5)
print(s5)

#remove

s5.remove(7)
print(s5)


#pop

s5.pop()
print(s5)

s5.clear()
print(s5)