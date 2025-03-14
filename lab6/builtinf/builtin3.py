def palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

text = "madam"
print(palindrome(text))
text = "hello"
print(palindrome(text))