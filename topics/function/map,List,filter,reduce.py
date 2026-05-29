print(list(map(lambda x:x**2 , [1,2,3,4])))

L=[1,2,3,4,5,6]

print(list(map(lambda x:'even'if x%2==0 else 'odd',L)))

print(list(filter(lambda x:x>2,L)))

import functools

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
)

print(functools.reduce(lambda x,y:x if x<y else y,[22,11,45,10,4]))
print(functools.reduce(lambda x,y:x if x>y else y,[22,11,45,10,4]))
