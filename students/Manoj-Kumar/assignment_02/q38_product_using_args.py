
def multiply(*numbers):

    product = 1

    for i in numbers:
        product = product * i

    return product


print(multiply(2, 3, 4))