import re

def m_sequence(text):
    pattern = r"^a.*b$"
    if re.fullmatch(pattern, text):
        return "match found"
    else:
        return "no match"
    
strings = [
    "ab",
    "acb",
    "a123b",
    "aXVZb",
    "a_b",
    "anc123b",
    "xyzab",
    "a_bc_def_b",
    "bca",
]

for s in strings:
    print(m_sequence(s))

"""
match found
match found
match found
match found
match found
match found
no match
match found
no match
"""