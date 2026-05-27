s= input('enter a string: ')

term =input('what term do you want to search: ')

counter =0

for i in s:
  if i == term:
    counter+=1

print('number of times term is present: ',counter)