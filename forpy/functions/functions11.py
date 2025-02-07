def pchecker(word):
    word = word.replace(" ", "").lower()
    return word==word[::-1]

print(pchecker("madam"))

