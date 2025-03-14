import time
import math

def d(number, milseconds):
    time.sleep(milseconds/1000)
    return math.sqrt(number)

num = int(input())
delay = int(input())
result = d(num, delay)
print(f"Square root of {num} after {delay} is {result}")