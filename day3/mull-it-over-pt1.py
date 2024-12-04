import re

def mul(x, y):
    return x * y

total = 0
with open('day3\\input.txt','r') as file:
    content = file.read()
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern,content)

    for match in matches:
        total = total + eval(match)

    print(total)