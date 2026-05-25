#menu driven calculator

num1= int (input("enter the first number: "))
num2= int (input("enter the second number: "))

operation= input("enter the operation you want to perform: ")
if operation == "+":
    print("the sum is: ",num1+num2)
elif operation == "-":
    print("the difference is: ",num1-num2)
elif operation == "*":
    print("the product is: ",num1*num2)
elif operation == "/":
    print("the quotient is: ",num1/num2)    
else:    print("invalid operation")