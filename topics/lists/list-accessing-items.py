L =([1,2,3,4,5])
#positive indexing
print(L[0])
L1=([[[1,2,3]],[[1,5,3],[4,5,6],[7,8,9]]])

print(L1[0][0][1]) # prints 2

#negative indexing

print(L[-1])

#slicing
print(L[1:4]) # prints elements from index 1 to 3

print(L1[1][0:2]) # prints [[1,5,3],[4,5,6]]

print(L[-3:-1])