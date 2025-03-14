def generate_squares(N):
    for number in range(1, N + 1):
        yield number ** 2

N = 5
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)

"""
1
4
9
16
25
"""