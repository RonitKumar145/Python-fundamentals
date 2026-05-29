def multiply(*args):
    product = 1

    for num in args:
        product *= num

    return product

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

print(multiply(*nums))

""""""