def sq(x):
  return x**2

def trans(f,l):
  output =[]
  for i in l:
    output.append(f(i))

  print(output)

l=[1,2,3,4,5,6]

print(trans(lambda x:x**2,l))