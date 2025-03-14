import re
def m_sequence(text):
    pattern = r"\b[A-Z][a-z]*\b"
    matches = re.findall(pattern, text)
    return matches

strings = [
    "Hello World",
    "Python regex",
    "hello World",
    "HELLO WORLD",
    "A b C d",
    "RegexIsCool",
]

for s in strings:
    print(m_sequence(s))

"""
['Hello', 'World']
['Python']
['World']
[]
['A', 'C']
[]
"""