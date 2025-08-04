import re

def tokenize(code):
    return re.findall(r"\w+|\S", code)