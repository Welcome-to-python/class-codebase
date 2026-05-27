while True:
    try:
        n = int(input())

        print(n)

        break

    except ValueError:
        print("Enter integer only")