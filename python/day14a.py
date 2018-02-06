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

total1s = 0
for lineNo in range(128):
    line = applyHash("oundnydw-"+str(lineNo), 256)
    lineHexValues = [line[i:i+2] for i in range(0, len(line), 2)]
    print line
    print lineHexValues
    print int('d4', 16)

    lineIntValues = map(lambda x: int(x, 16), lineHexValues)
    print lineIntValues
    lineBinaryValues = map(lambda x:bin(x)[2:].zfill(8), lineIntValues)
    print lineBinaryValues

    total1s += reduce(lambda x,y: str(x)+str(y), lineBinaryValues).count("1")

print total1s
