try:
    with open(r"D:\Workspace\Python_of_Classmates\pavan_python\class-codebase\students\PavanVastrad\assignment_01\sample.txt", "r") as file:
        text = file.read()
        words = text.split()
        print("Word count:", len(words))

except FileNotFoundError:
    print("File not found. Check the path.")