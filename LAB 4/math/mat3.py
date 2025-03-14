import math

def area_polygon(n, s):
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    area = round((n * s**2) / (4 * math.tan(math.pi / n)))
    return area

n = int(input("Input the number of sides: "))
s = int(input("Input the length of a side: "))
print(f"The area of the polygon is: {area_polygon(n, s)}")
"""
Input the number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""