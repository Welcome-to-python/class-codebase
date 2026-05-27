##Swap the values of two variables without using a third temporary variable.

a=10
b=20
print("Before:")

print(f"a is {a}")
print(f"b is {b}")

a,b=b,a
print("After:")


print(f"a is {a}")
print(f"b is {b}")

