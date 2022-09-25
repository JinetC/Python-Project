from math import pi

r = float(input("enter the radius of the circle:"))


def circle_area(r):
    c = pi * r ** 2
    return c


print("Area of a circle is", round(circle_area(r), 4))
