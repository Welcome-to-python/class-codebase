rows = 3

# Upper triangle
for i in range(1, rows + 1):
    # spaces
    for j in range(rows - i):
        print(" ", end="")

    # stars
    for k in range(i):
        print("* ", end="")

    print()

# Lower triangle
for i in range(rows - 1, 0, -1):
    # spaces
    for j in range(rows - i):
        print(" ", end="")

    # stars
    for k in range(i):
        print("* ", end="")

    print()
