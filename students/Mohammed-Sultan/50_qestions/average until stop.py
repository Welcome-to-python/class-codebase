total = 0
count = 0

while True:
    x = input()

    if x == "stop":
        break

    total += int(x)
    count += 1

print(total / count)