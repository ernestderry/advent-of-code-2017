disk = []
rangeMap = {}
rangeCount = 0

def buildList(size):
    knotHash = []
    for n in range(size):
        knotHash.append(n)
    return knotHash

def rotateList(knotHash, currentPos, length):

    knotHashLength = len(knotHash)

    overFlow = currentPos + length - knotHashLength

    if overFlow > 0:
        overFlowSpan = knotHash[0:overFlow]
        span = knotHash[currentPos:]
    else:
        overFlowSpan = []
        span = knotHash[currentPos:currentPos+length]

    span.extend(overFlowSpan)
    reversedSpan = span[::-1]

    pos = currentPos
    for n in reversedSpan:
        if pos > (knotHashLength - 1):
            pos = 0
        knotHash[pos] = n
        pos += 1

    return knotHash

def getAsciiChars(lengthString):
    return [ord(c) for c in lengthString]

def applyHash(lengthString, knotHashLength):
    lengthsAscii = getAsciiChars(lengthString)
    lengthsAscii.extend([17, 31, 73, 47, 23])

    knotHash = buildList(knotHashLength)
    currentPos = 0
    skip = 0
    for times in range(64):
        for ln in lengthsAscii:
           rotateList(knotHash, currentPos, ln)
           currentPos = currentPos + ((ln + skip) % knotHashLength)
           if currentPos > (knotHashLength - 1) :
               currentPos = currentPos - knotHashLength
           skip += 1

    chunks = [knotHash[p:p+16] for p in range(0, 256, 16)]
    denseHash = [reduce(lambda x, y: x ^ y, c) for c in chunks]

    hexString = ""
    for x in denseHash:
        hexValue = "0" + hex(x)[2:]
        hexString += hexValue[-2:]

    return hexString

def cellUsed(cell):
    return disk[cell[1]][cell[0]] == "1"

def tryCell(nextCell, rangeCount):
    if cellUsed(nextCell):
        if nextCell not in rangeMap:
            markCellAndNeighbours(nextCell, rangeCount)

def markCellAndNeighbours(cell, rangeCount):
    rangeMap[cell] = rangeCount
    if cell[1] > 0:
        nextCell = (cell[0], cell[1]-1)
        tryCell(nextCell, rangeCount)

    if cell[1] < 127:
        nextCell = (cell[0], cell[1]+1)
        tryCell(nextCell, rangeCount)

    if cell[0] > 0:
        nextCell = (cell[0]-1, cell[1])
        tryCell(nextCell, rangeCount)

    if cell[0] < 127:
        nextCell = (cell[0]+1, cell[1])
        tryCell(nextCell, rangeCount)

def addCellToNewRange(cell):
    global rangeCount
    rangeCount += 1
    markCellAndNeighbours(cell, rangeCount)

print "building disk image"
for lineNo in range(128):
    line = applyHash("oundnydw-"+str(lineNo), 256)
    lineHexValues = [line[i:i+2] for i in range(0, len(line), 2)]
    lineIntValues = map(lambda x: int(x, 16), lineHexValues)
    lineBinaryValues = map(lambda x:bin(x)[2:].zfill(8), lineIntValues)

    disk.append(reduce(lambda x,y: str(x)+str(y), lineBinaryValues))

print "counting ranges"

for line in range(128) :
    for col in range(128):
        cell = (col, line)
        if cellUsed(cell):
            if cell not in rangeMap:
                addCellToNewRange(cell)

print "number of ranges "+str(rangeCount)
