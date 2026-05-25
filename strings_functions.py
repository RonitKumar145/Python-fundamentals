#len,max,min,sorted

len('hello world')
#output=11

max('helloworld')
#output=w

min('helloworld')
#output=d
sorted('hello world')
#output=[' ', 'd', 'e', 'h', 'l', 'l', 'o', 'o', 'r', 'w']

sorted('hello world',reverse=True)
#output=['w', 'r', 'o', 'o', 'l', 'l', 'h', 'e', 'd', ' ', 'd']


s= 'hello world'
s.capitalize()
#Hello World

s.title()
#Hello World
s.upper()
#HELLO WORLD
s.lower()
#hello world
'heLlo World'.swapcase()
#HElLO wORLD


'my name is ronit'.count('i')
#output=2

'my name is ronit'.find('i')
#output=17
'my name is ronit'.index('i')
#output=17

'my name is ronit'.startswith('my')
#output=True

'my name is ronit'.endswith('ronit')
#output=True

name ='ronit'

gender ='male'

'hi my name is {} and i am a {}'.format(name,gender)
#output=hi my name is ronit and i am a male 
