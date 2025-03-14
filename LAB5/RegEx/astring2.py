import re
def m_string(text):
    pattern = r"^ab{2,3}$"
    if re.fullmatch(pattern, text):
        return "match found"
    else:
        return "no match"

strings = ["a", "ab", "abb", "abbb", "b", "c", "aaa", "aabbbba"]
for s in strings:
    print(m_string(s))   

"""
no match
no match
match found
match found
no match
no match
no match
no match
"""