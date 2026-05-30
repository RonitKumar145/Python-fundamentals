#create numpy arrays

#np.array

import numpy as np

a=np.array([1,2,3])
print(type(a))

#2d and 3d
b=np.array([[1,2,3],[4,5,6]])

print(b)

c=np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(c)

print(np.array([1,2,3],dtype =complex))
#arange

print(np.arange(1,11,2))
#reshape

print(np.arange(1,13).reshape(4,3))

#np.ones and np.zeros
x=np.ones((3,4))
print(x)

y= np.zeros((3,4))
print(y)

#np.random
z=np.random.random((3,4))
print(z)

#np.linspace linear space

print(np.linspace(-10,10,10))

#np.identify

print(np.identity(3)) 