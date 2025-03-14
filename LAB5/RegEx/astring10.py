import re


def c_to_s(text):
    return re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower()

strings = [
    "helloWorld",
    "PythonIsFun",
    "ConvertThisText",
    "CamelCaseString",
]

for s in strings:
    print(c_to_s(s))

"""
hello_world
python_is_fun
convert_this_text
camel_case_string
"""