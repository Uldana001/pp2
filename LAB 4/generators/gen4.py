def squares(a, b):
    for number in range(a, b + 1):
        yield number ** 2

a = 2
b = 5

for square in squares(a, b):
    print(square)

"""
4
9
16
25
"""