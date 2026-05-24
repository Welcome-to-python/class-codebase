try:
    with open(r"D:\Workspace\Python_of_Classmates\Arpit_python\class-codebase\students\Arpit-Raj\assigment_01\sample.txt", "r") as file:
        text = file.read()
        words = text.split()
        print("Word count:", len(words))

except FileNotFoundError:
    print("File not found. Check the path.")