import re

def f_sequence(text):
    pattern = r"\b[a-z]+(?:_[a-z]+)+\b"
    if re.fullmatch(pattern, text):
        return "match found"
    else:
        return "no match"

test_string = [
    "hello_world",
    "python_regex",
    "hello_World",
    "hello123_world",
    "no_match",
    "test_case_example"
]

for s in test_string:
    print(f_sequence(s))

"""
match found
match found
no match
no match
match found
match found
"""