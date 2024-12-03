file = open('H:\Work\python\\aoc2024\day2\input','r')

list = []
safeTotal = 0

for line in file.readlines():
    numbers = line.split(' ')
    symbol = False
    initialSymbol = False
    for i in range(0,len(numbers)-1):
        diff = int(numbers[i + 1]) - int(numbers[i])
        if(i == 0): initialSymbol = diff > 0
        symbol = diff > 0
        if(abs(diff) < 1 or abs(diff) > 3 or (initialSymbol != symbol)): break
        elif(i == len(numbers)-2): safeTotal = safeTotal + 1
            
print(safeTotal)