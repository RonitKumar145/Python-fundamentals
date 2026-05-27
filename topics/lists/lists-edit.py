#s ='hello'#
#s[0] = 'H' # This will raise an error because strings are immutable
L =[1,2,3,4,5]
L[0] = 10 # This will work because lists are mutable
print(L) # prints [10, 2, 3, 4, 5]

L[-1] = 20 # This will change the last element of the list to 20
print(L) # prints [10, 2, 3, 4, 20]

L[1:3] = [30, 40] # This will replace the elements at index 1 and 2 with 30 and 40
print(L) # prints [10, 30, 40, 4, 20]

#del
print('del')
l = [1,2,3,4,5]
del l[0] # This will delete the element at index 0
print(l) # prints [2, 3, 4, 5]
del l[1:3] # This will delete the elements at index 1 and 2
print(l) # prints [2, 5]  

#remove
print('remove')
l = [1,2,3,4,5]
l.remove(3) # This will remove the first occurrence of 3 from the list
print(l) # prints [1, 2, 4, 5]

#pop
print('pop')
l = [1,2,3,4,5]
l.pop() # This will remove and return the last element of the list
print(l) # prints [1, 2, 3, 4]
l.pop(1) # This will remove and return the element at index 1
print(l) # prints [1, 3, 4]

#clear
print('clear')
l = [1,2,3,4,5]
l.clear() # This will remove all elements from the list
print(l) # prints []
