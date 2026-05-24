def positive_numbers(numbers):

    result = []

    for num in numbers:
        if num > 0:
            result.append(num)

    return result


numbers = [-5, 10, -2, 7, 0, 15]

print(positive_numbers(numbers))