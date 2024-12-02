import fileinput

file = open('H:\Work\python\\aoc2024\day1\input','r')

list1 = []
list2 = []

for line in file.readlines():
    lineList = line.split('   ')
    list1.append(lineList[0])
    list2.append(lineList[1].replace('\n',''))

numOcc = 0
simScore = 0
for item in list2:
    numOcc = list1.count(item)
    simScore = simScore + (numOcc * int(item))

print(simScore)

