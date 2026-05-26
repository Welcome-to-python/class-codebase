
#using to loop

# rows = 5

# for i in range(1, rows + 1):

#     for j in range(rows - i):
#         print(" ", end="")

#     for k in range(2 * i - 1):
#         print("*", end="")

#     print()

#using one loop

# rows = 5

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "*" * (2 * i - 1))

#method 3

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * (2 * i - 1))