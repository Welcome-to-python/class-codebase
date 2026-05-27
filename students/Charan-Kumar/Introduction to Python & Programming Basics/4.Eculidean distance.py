#Calculate the Euclidean distance between two points (x1, y1) and (x2, y2) using basic
#arithmetic operators and the exponentiation operator (**).  

# Euclidean Distance Program

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Euclidean Distance =", distance)

