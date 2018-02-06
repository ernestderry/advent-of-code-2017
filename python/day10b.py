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

print "null " + str(applyHash("", 256) == "a2582a3a0e66e6e86e3812dcb672a272")
print "AoC " + str(applyHash("AoC 2017", 256) == "33efeb34ea91902bb2f59c9920caa6cd")
print "1,2,3 " + str(applyHash("1,2,3", 256) == "3efbe78a8d82f29979031a4aa0b16a9d")
print "1,2,4 " + str(applyHash("1,2,4", 256) == "63960835bcdc130f0b66d7ff4f6a5a8e")
print "answer " + str(applyHash("230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167", 256) == "0c2f794b2eb555f7830766bf8fb65a16")
