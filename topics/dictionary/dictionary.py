#empty

s={}
print(type(s))

d1 = { 'name':'ronit','gender':'male'}

d2={(1,2,3):1,'name':'ronit'}

d3={
  'name':'ronit',
  'subject':{'dsa':50,'maths':50}
}
print(d3)

print(d2)

print(d1)


d4=dict([(1,1),(2,2),(3,3)])
print(d4)

#cannot have multiple items as keys
#mutable items as keys are not allowed

#no indexxing concept

print(d3['name'])
print(d3.get('name'))


d3['type']='hot'
print(d3)

d3['type']='hot'
print(d3)

d3.pop('type')
print(d3)

d3.popitem()
print(d3)

del d3['name']

print(d3)

d1.clear()
print(d1)