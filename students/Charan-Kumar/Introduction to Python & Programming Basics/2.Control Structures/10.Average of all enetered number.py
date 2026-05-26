total = 0
count = 0

while True:
    x = input("Enter a number (or stop): ")

    if x == "stop":
        break

    total += float(x)
    count += 1

print("Average =", total / count)