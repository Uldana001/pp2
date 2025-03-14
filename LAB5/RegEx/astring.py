import re
def m_string(text):
    pattern = r'^a*b*$'
    if re.fullmatch(pattern, text):
        return "match found"
    else:
        return "no match"
    
strings = ["a", "ab", "abb", "aabb", "b", "c", "aaa", "aabbbba"]
for s in strings:
    print(m_string(s))


"""
match found
match found
match found
match found
match found
no match
match found
no match
"""