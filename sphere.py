"""
File: sphere.py
Author: Jasmin Husidic
Description: A program to calculate the circumference of a sphere given it's radius.
"""

import math

radiusString = input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)
diameter = 2 * radiusInteger
surfacearea = (4 * math.pi) * (radiusInteger ** 2)
volume = (4/3 * math.pi) * (radiusInteger ** 3)

print("The circumference is: ",circumference)
print("The area is:",area)
print("The diameter is:",diameter)
print("The surface area is:",surfacearea)
print("The volume is:", volume)



