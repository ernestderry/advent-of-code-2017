def redistributeCycle(blockList):
    newBlockList = list(blockList)

    highest = 0
    highestPos = 0
    numberOfBlocks = len(blockList)
    for b in range(numberOfBlocks):
        if newBlockList[b] > highest:
            highest = blockList[b]
            highestPos = b

    allBlocksGet = int(highest/numberOfBlocks)
    remainder = highest % numberOfBlocks

    newBlockList[highestPos] = 0

    for b in range(numberOfBlocks):
        newBlockList[b] += allBlocksGet

    b = highestPos + 1
    while remainder > 0:
        if b > (numberOfBlocks - 1):
            b = 0
        newBlockList[b] += 1
        remainder -= 1
        b += 1
    return newBlockList


def countRedistributions(block):
    blockList = map(int, block.split())

    fullList = []
    cycles = 0
    while True:
        print blockList
        cycles += 1
        fullList.append(blockList)
        blockList = redistributeCycle(blockList)
        if fullList.count(blockList) > 0:
            break

    return cycles


print redistributeCycle([0, 2, 7, 0]) == [2, 4, 1, 2]

print countRedistributions("0 2 7 0")

print countRedistributions("4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3")
