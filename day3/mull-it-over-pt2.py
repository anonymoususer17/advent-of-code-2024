import re

def mul(x, y):
    return x * y

total = 0
with open('day3\\input.txt','r') as file:
    content = file.read()
    initDoList = content.split('do()')
    print(len(initDoList))
    
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    
    for doSeq in initDoList:
        doSeq = doSeq.split('don\'t()')
        matches = re.findall(pattern,doSeq[0])

        for match in matches:
            total = total + eval(match)

    print(total)