s= input('enter a string: ')

term =input('what term do you want to remove: ')

result =" "

for i in s:

  if i != term:
    result= result +i

print('string after removing term is: ',result)

