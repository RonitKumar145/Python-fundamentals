s=input('enter string: ')

for i in range(0,len(s)//2):
  if s[i] != s[len(s)-1-i]:
    print('string is not a pallindrome')
    break
else:
  print('string is a pallindrome')  