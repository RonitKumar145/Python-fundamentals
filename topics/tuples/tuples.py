#empty
t1 =()
print(t1)
#create a tuple with a single item 
t2 =('hello',)
print(type(t2))

# homo

t3 =(1,2,3,4)
print(t3)

#hetro

t4 = (1,5.4,'true',[2,3,4])
print(t4)

#using type conversion

t5 = tuple('hello')
print(t5)

#tuples are immutable
#so no addition or editing allowed

#delition happens only to whole tuple and not just a section

t7=(1,2,3,4,5,6)

del t7

print (t7)