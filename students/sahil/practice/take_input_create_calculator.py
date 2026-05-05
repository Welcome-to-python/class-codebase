num1 = int(input("enter the number : "))

num2 = int(input("enter the number: "))

oper  = input("enter the operator (+,-,*,/): ")

if oper == '+':
    print(num1 + num2)


elif oper == '-':
    print(num1-num2)

elif oper == '*':
    print(num1*num2)

elif oper == '/':
    print(num1/num2)

else:
    print("Invalid Input")
