age = int(input("Enter your Age: "))

if age > 100:
    print("RIP")
elif age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")