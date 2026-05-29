def f(i):
    """
    orinyjbdvbb"""
    if i % 2 == 0:
        return "even"
    return "odd"

try:
    i = int(input("Enter a number: "))
    print(f(i))
except ValueError:
    print("Please enter a valid integer.")

print(f.__doc__)