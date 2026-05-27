def product(*args):
    result = 1
    for i in args:
        result *= i
    return result

# User input
nums = map(int, input("Enter numbers separated by space: ").split())

print("Product =", product(*nums))