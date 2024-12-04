file = open('day2\\input','r')

# Initialize variables
safeTotal = 0

#  Loop over all lines in the input
for line in file.readlines():
    # Split the lines by space (get all numbers)
    numbers = line.split(' ')

    # Initialize a list of pairs, one for differences and the other for level (increase or decrease)
    pairList = []

    # Loop over all numbers in one line
    for i in range(0,len(numbers)-1):
        # Calculate the difference, append it to the list and also if its positive or negative
        diff = int(numbers[i+1]) - int(numbers[i])
        if diff > 0:
            level = 1
        if diff < 0:
            level = -1
        if diff == 0:
            level = 0 
        pairList.append([diff, level])

    # Check all the differences, there should not be any greater than 3 or less than 1
    toleranceIndex = 1000
    noMore = False
    for i in range(0, len(pairList)):
        absDiff = abs(pairList[i][0])
        if(absDiff < 1 or absDiff > 3):
            if(toleranceIndex == 1000): toleranceIndex = i
            else: 
                noMore = True
                continue
            
    if(noMore == True): continue
    
    # Check all the levels, they should all be the same
    pozCount = 0
    negCount = 0
    negIndex = 0
    pozIndex = 0
    neutralCount = 0
    neutralIndex = 0
    for i in range(0, len(pairList)):
        if(pairList[i][1] == 1): 
            pozCount = pozCount + 1
            pozIndex = i
        elif pairList[i][1] == -1: 
            negCount = negCount + 1
            negIndex = i
        else:
            neutralCount = neutralCount + 1
            neutralIndex = i
    if(pozCount < len(pairList) - 1 and negCount < len(pairList) - 1): continue
    elif(negCount == 1 and toleranceIndex == negIndex): pairList.remove(pairList[toleranceIndex])
    elif(pozCount == 1 and toleranceIndex == pozIndex): pairList.remove(pairList[toleranceIndex])
    elif(neutralCount == 1 and toleranceIndex == neutralIndex): pairList.remove(pairList[toleranceIndex])
    elif(toleranceIndex < 1000): pairList.remove(pairList[toleranceIndex])

    if(pozCount < len(pairList) and negCount < len(pairList)): continue

    for i in range(0, len(pairList)):
            absDiff = abs(pairList[i][0])
            if(absDiff < 1 or absDiff > 3):
                continue
    symbol = False
    initialSymbol = False
    for i in range(0,len(pairList)-1):
        diff = int(pairList[i][0])
        if(i == 0): initialSymbol = diff > 0
        symbol = diff > 0
        if(abs(diff) < 1 or abs(diff) > 3 or (initialSymbol != symbol)): continue
        elif(i == len(pairList)-2): safeTotal = safeTotal + 1
    
            
print(safeTotal)