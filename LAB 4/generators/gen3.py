def generator(n):
    for number in range(n+1):
        if number%3==0 and number%4==0:
            yield number

try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        raise ValueError("The number must be non-negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    nums = generator(n)
    nums_str = ','.join(map(str, list(nums)))
    print(nums_str)

"""
Enter a non-negative integer: 143
0,12,24,36,48,60,72,84,96,108,120,132
"""