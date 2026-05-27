#append

l =[1,2,3,4,5]

l.append(6)
print(l)


#extend

l1 =[1,2,3]
l1.extend([4,5,6] )
print(l1)

l2 =[1,2,3]
l2.extend("hello" )
print(l2) #prints [1, 2, 3, 'h', 'e', 'l', 'l', 'o']

#insert

l2 =[1,2,3,4,5]
l2.insert(2,10) # inserts 10 at index 2
print(l2)