n =int(input('enter n'))
result =0 
fat =1  
for i in range(1,n+1):
  fat = fat *i
  result = result + i/ fat

  print(result)