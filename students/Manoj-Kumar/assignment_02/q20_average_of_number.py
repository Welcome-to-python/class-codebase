
total = 0
count = 0

while True:
    num = input("Enter number (or stop): ")

    if num == "stop":
        break

    total = total + int(num)
    count = count + 1

print("Average =", total / count)