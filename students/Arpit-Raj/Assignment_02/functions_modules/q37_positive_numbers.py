def positive_numbers(numbers):

    result = []

    for number in numbers:

        if number > 0:
            result.append(number)

    return result


numbers = [-2, 5, -1, 8, 10]

print(positive_numbers(numbers))
