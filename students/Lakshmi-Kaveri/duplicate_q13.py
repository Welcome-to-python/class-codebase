my_list = [1, 2, 3, 2, 4, 5, 6]
duplicates =[]
for num in my_list:
    if my_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
        print("Duplicate elements:", duplicates)