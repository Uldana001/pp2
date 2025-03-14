def even_numbers_generator(n):
    for number in range(0, n + 1, 2):
        yield number

try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        raise ValueError("The number must be non-negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    even_numbers = even_numbers_generator(n)
    even_numbers_str = ','.join(map(str, even_numbers))
    print(even_numbers_str)

"""
Enter a non-negative integer: 5
0,2,4
"""