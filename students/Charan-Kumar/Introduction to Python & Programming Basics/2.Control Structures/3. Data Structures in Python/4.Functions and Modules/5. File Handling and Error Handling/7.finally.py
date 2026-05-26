try:
    file = open("sample.txt", "r")

    data = file.readlines()
    print(data)

except FileNotFoundError:
    print("File not found!")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("No file to close.")