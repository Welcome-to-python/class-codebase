import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# User input
r = float(input("Enter radius: "))

print("Volume of Sphere =", sphere_volume(r))