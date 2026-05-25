import math


def sphere_volume(radius):

    volume = (4 / 3) * math.pi * radius ** 3

    return volume


radius = float(input("Enter radius: "))

print("Volume of Sphere:", sphere_volume(radius))
