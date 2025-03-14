import re

def space(text):
    return re.sub(r'(?<=\w)([A-Z][a-z])', r' \1', text)


strings = [
    "HelloWorld",
    "PythonIsFun",
    "InsertSpacesNow",
    "UPPERCaseTest",
]

for s in strings:
    print(space(s))
"""
Hello World
Python Is Fun
Insert Spaces Now
UPPER Case Test
"""