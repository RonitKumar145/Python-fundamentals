#add 1 to 10 numbers to a list using list comprehension
l =[]

for i in range(1,11):
  l.append(i)

print(l) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l=[i for i in range (1,11)]
print(l) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#scalar multiplication on a vector using list comprehension
v = [1,2,3,4,5]
s = 2
x = []
for i in  v:
  x.append(i*s)
print(x) # prints [2, 4, 6, 8, 10]

v = [1,2,3,4,5]
s = 2
print([s*i for i in v]) # prints [2, 4, 6, 8, 10]

#add squares
l=[1,2,3,4,5]

print([i**2 for i in l])


#print all numbers divisible by 5 in the range od 1 to 50

print([i for i in range(1,51) if i % 5 ==0])

#find languages which start with letter j

languages =['java','cpp','javascript','python','c','php']

print([languages for languages in languages if languages.startswith('j')])

#nested if with list comprehension

basket= ['apple','guava','cherry','banana']
my_fruits=['apple','guava','cherry','grapes','kiwi']

# add new list from my fruits and items if the fruit exists in basket and also starts with a

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a') ])


#print a (3,3) matrix using list comprehension
print([[i*j for i in range (1,4)] for j in range (1,4)])

#cartesian prodeucts -> list comprehension on 2 lists together
l1=[1,2,3,4]
l2=[5,6,7,8]

print([i*j for i in l1 for j in l2])

#2 ways to travelse lists

#itemwise

l= [1,2,3,4]
for i in l:
  print(i)


#indexwise

l=[1,2,3,4]

for i in range(0,len(l)):
  print (i)

