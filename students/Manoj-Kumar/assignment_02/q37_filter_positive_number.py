
def positive_numbers(numbers):

    positive = []

    for i in numbers:
        if i > 0:
            positive.append(i)

    return positive


list1 = [-2, 5, -1, 8, 10]

print(positive_numbers(list1))