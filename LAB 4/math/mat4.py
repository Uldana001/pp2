def area_base_height(base, height):
    return base * height

base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = float(area_base_height(base, height))
print(f"Expected output: {area}")
"""
Length of base: 5
Height of parallelogram: 6
Expected output: 30.0
"""