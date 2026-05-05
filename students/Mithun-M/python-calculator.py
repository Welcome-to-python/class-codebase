operator=input("enter an operator (+,-,/,*):")
n1=float(input("ënter an number"))
n2=float(input("other one"))
if operator=="+":
    result=n1+n2
    print(round(result,2))
elif operator=="-":
    result=n1-n2
    print(round(result,3))
elif operator=="/":
    result=n1/n2 or n2/n1
    print(round(result,3))
elif operator=="*":
    result=n1*n2
    print(round(result,2))
else:
    print(f"you type wrong operator")