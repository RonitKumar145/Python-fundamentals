#len/min/max/sorted

L = [3, 1, 4, 1, 5, 9]
print(len(L)) # This will print the length of the list L, which is 6
print(min(L)) # This will print the minimum value in the list L, which is
print(max(L)) # This will print the maximum value in the list L, which is 9
print(sorted(L)) # This will print a new list that is a sorted version of L, which is [1, 1, 3, 4, 5, 9]


#count
L = [1, 2, 3, 4, 5, 1, 2, 3]
print(L.count(1)) # This will count the number of occurrences of 1 in the list L, which is 2
print(L.count(2)) # This will count the number of occurrences of 2 in the list L, which is 2
print(L.count(3)) # This will count the number of occurrences of 3 in the list L, which is 2
print(L.count(4)) # This will count the number of occurrences of 4 in the list L, which is 1

# index
L = [1, 2, 3, 4, 5, 1, 2, 3]
print(L.index(1)) # This will return the index of the first occurrence of 1 in the list L, which is 0
print(L.index(2)) # This will return the index of the first occurrence of 2 in the list L, which is 1


#reverse

L = [1, 2, 3, 4, 5]
L.reverse() # This will reverse the list L in place
print(L) # This will print the reversed list, which is [5, 4, 3, 2, 1]


#sort vs sorted
L = [3, 1, 4, 1, 5, 9]
L.sort() # This will sort the list L in place
print(L) # This will print the sorted list, which is [1, 1, 3, 4, 5, 9]
L = [3, 1, 4, 1, 5, 9]
sorted_L = sorted(L) # This will create a new sorted list from L
print(sorted_L) # This will print the new sorted list, which is [1, 1, 3, 4, 5, 9]


#copy
L = [1, 2, 3, 4, 5]
L_copy = L.copy() # This will create a shallow copy of the list L
print(L_copy) # This will print the copied list, which is [1, 2, 3, 4, 5]


#zip func

l1=[1,2,3,4]
l2=[-1,-2,-3,-4]

list(zip(l1,l2))

print([i+j for i,j in zip(l1,l2)])