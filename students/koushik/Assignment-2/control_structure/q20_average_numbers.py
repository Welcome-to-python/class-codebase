total = 0
count = 0

while True:
    value = input("Enter a number (or type stop): ")

    if value.lower() == "stop":
        break

    number = float(value)
    total += number
    count += 1

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers entered.")