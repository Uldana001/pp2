import math

class Stringer:
    def __init__(self, text):
        self.text = text

    def getString (self):
        self.text = input("Enter the text: ")
        print("Text updated")

    def printString(self):
        print(self.text)

a = Stringer("testssada")
a.printString()

a.getString()

a.printString()