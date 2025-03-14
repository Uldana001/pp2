import re

def split_u(text):
    return re.findall(r'[A-Z][a-z]*', text)


strings=[
    "HelloWorld",
    "PythinIsFun",
    "SplitAtUppercase",
    "CamelCaseString",
    "UPPER",
]

for s in strings:
     print(f"Original: {s}  →  Split: {split_u(s)}")

"""
Original: HelloWorld  →  Split: ['Hello', 'World']
Original: PythinIsFun  →  Split: ['Pythin', 'Is', 'Fun']
Original: SplitAtUppercase  →  Split: ['Split', 'At', 'Uppercase']
Original: CamelCaseString  →  Split: ['Camel', 'Case', 'String']
Original: UPPER  →  Split: ['U', 'P', 'P', 'E', 'R']
"""

