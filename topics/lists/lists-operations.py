#arithemetic operations
L1=[1,2,3]
L2=[4,5,6]

print(L1 + L2) # This will concatenate the two lists and print [1, 2, 3, 4, 5, 6]
print(L1 * 2) # This will repeat the list L1 twice and print [1, 2, 3, 1, 2, 3] 

#membership operations
L = [1, 2, 3, 4, 5]
print(3 in L) # This will check if 3 is in the list L and print True
print(6 in L) # This will check if 6 is in the list L and print False
print(3 not in L) # This will check if 3 is not in the list L and print False
print(6 not in L) # This will check if 6 is not in the list L and print True


#loops
L = [1, 2, 3, 4, 5]
for i in L:
    print(i) # This will print each item in the list L on a new line