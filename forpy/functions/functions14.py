def is_palindrome(word):
    if word==word[::-1]:
        return True

def contains_palindrome(sentence):
    words = sentence.split()
    for word in words:
        if is_palindrome(word):
            return True
    return False

print(contains_palindrome("Hello madam how are you"))