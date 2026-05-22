numbers = []

while True:

    value = input("Enter a number or type stop: ")

    if value.lower() == "stop":
        break

    numbers.append(float(value))

average = sum(numbers) / len(numbers)

print("Average:", average)
