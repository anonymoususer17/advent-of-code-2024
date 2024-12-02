import fileinput

file = open('H:\Work\python\\aoc2024\day1\input','r')

list1 = []
list2 = []

for line in file.readlines():
    lineList = line.split('   ')
    list1.append(lineList[0])
    list2.append(lineList[1].replace('\n',''))

list1.sort()
list2.sort()

totaldistance = 0

for i in range(0,len(list1)):
    totaldistance = totaldistance + abs(int(list1[i]) - int(list2[i]))

print(totaldistance)

