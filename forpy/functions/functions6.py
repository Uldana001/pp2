def reversed_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    return reversed_sentence

s = input()
print(reversed_words(s))