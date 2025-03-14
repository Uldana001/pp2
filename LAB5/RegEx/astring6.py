import re

def r_sequence(text):
    pattern = r"[ ,.]"
    return re.sub(pattern, ":", text)

strings = [
    "Hello, world. This is python",
    "python is fun. let's code!",
    "hello world, how are you?",
    "A, B, C. D E F",
]

for s in strings:
    print(f"Original: {s}")
    print(f"Modified: {r_sequence(s)}")

"""
Original: Hello, world. This is python
Modified: Hello::world::This:is:python
Original: python is fun. let's code!
Modified: python:is:fun::let's:code!
Original: hello world, how are you?
Modified: hello:world::how:are:you?
Original: A, B, C. D E F
Modified: A::B::C::D:E:F
"""