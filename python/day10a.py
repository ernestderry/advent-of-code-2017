def buildList(size):
    knotHash = []
    for n in range(size):
        knotHash.append(n)
    return knotHash


def rotateList(knotHash, currentPos, length):
    knotHashLength = len(knotHash)

    overFlow = currentPos + length - knotHashLength
    print "over flow " + str(overFlow)
    if overFlow > 0:
        overFlowSpan = knotHash[0:overFlow]
        span = knotHash[currentPos:]
    else:
        overFlowSpan = []
        span = knotHash[currentPos:currentPos+length]

    print "span " + str(span)
    print "over flow span " + str(overFlowSpan)
    span.extend(overFlowSpan)
    reversedSpan = span[::-1]
    print "reversed span " + str(reversedSpan)

    pos = currentPos
    for n in reversedSpan:
        if pos > (knotHashLength - 1):
            pos = 0
        knotHash[pos] = n
        pos += 1

    print "rotated " + str(knotHash)

    return knotHash

def applyHash(lengthString, knotHashLength):
    lengths = map(int, lengthString.split(","))
    knotHash = buildList(knotHashLength)
    currentPos = 0
    skip = 0
    for l in lengths:
       rotateList(knotHash, currentPos, l)
       currentPos = currentPos + l + skip
       if currentPos > (knotHashLength - 1) :
           currentPos = currentPos - knotHashLength
       skip += 1
    return knotHash


print "simple test " + str(applyHash("3,4,1,5", 5))
print "*****"
knotHash = buildList(5)
print rotateList(knotHash, 0, 0) == [0, 1, 2, 3, 4]

knotHash = buildList(5)
print rotateList(knotHash, 0, 3) == [2, 1, 0, 3, 4]

knotHash = buildList(5)
print rotateList(knotHash, 0, 5) == [4, 3, 2, 1, 0]

knotHash = buildList(5)
print rotateList(knotHash, 2, 1) == [0, 1, 2, 3, 4]

knotHash = buildList(5)
print rotateList(knotHash, 2, 2) == [0, 1, 3, 2, 4]

knotHash = buildList(5)
print rotateList(knotHash, 2, 3) == [0, 1, 4, 3, 2]

knotHash = buildList(5)
print rotateList(knotHash, 2, 4) == [2, 1, 0, 4, 3]

knotHash = buildList(5)
print rotateList(knotHash, 2, 5) == [3, 2, 1, 0, 4]

knotHash = buildList(5)
print rotateList(knotHash, 4, 1) == [0, 1, 2, 3, 4]

knotHash = buildList(5)
print rotateList(knotHash, 4, 2) == [4, 1, 2, 3, 0]

knotHash = buildList(5)
print rotateList(knotHash, 4, 3) == [0, 4, 2, 3, 1]

print "answer " + str(applyHash("230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167", 256))
