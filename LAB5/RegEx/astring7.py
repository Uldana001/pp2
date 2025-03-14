import re

def s_t_c(text):
    words = text.split('_')
    camel_case = words[0]+''.join(word.capitalize() for word in words[1:])
    return camel_case

string = [
    "hello_world",
    "this_is_python",
    "convert_snake_case",
    "snake_case_string",
]


for s in string:
    print(s_t_c(s))


"""
helloWorld
thisIsPython
convertSnakeCase
snakeCaseString
"""