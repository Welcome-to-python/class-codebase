weight=float(input("enter your weight~))
unit=input("Kilogram oR Pounds (K OR P)~")

if unit=="K":
    weight=weight*2.205
    unit="Lbs"
    print(f"the weight is converted into kilogram~{round(weight,3)} {unit}")
elif unit=="P":
    weight=weight/2.205
    unit="Kgs"
    print(f"the weight of yours is converted into pounds~{round(weight,3)} {unit}")
else:
    print(f"{unit} was not valid")
    
