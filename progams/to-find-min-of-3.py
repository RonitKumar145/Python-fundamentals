#find min of 3 nos
a= int (input("enter the first number: "))
b= int (input("enter the second number: "))
c= int (input("enter the third number: "))

if a<b and a<c:
    print("the smallest number is: ",a)
elif b<a and b<c:
    print("the smallest number is: ",b)
else:    print("the smallest number is: ",c)
