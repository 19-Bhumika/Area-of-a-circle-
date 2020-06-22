from math import pi
def area(r):
    return pi*r*r
radius=float(input("Input the radius of the circle:"))
print("The area of the circle with radius "+str(radius)+" is:"+ str(area(radius)))

