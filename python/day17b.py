def advance(slockLen, startPos, steps):
    stepsAfterFullRotations = steps % slockLen

    newPos = startPos + stepsAfterFullRotations
    if newPos > (slockLen - 1):
        newPos -= slockLen

    newPos += 1

    return newPos

pos = 0
slockLen = 1
for n in range(1, 50000001):
    pos = advance(slockLen, pos, 345)
    slockLen += 1
    if pos == 1:
        print n
        answer = n
    if n % 100000 == 0:
        print "done "+str(n)

print "answer "+ str(answer)

print
print "testing"

print 1 == advance(1, 0, 3)
print 1 == advance(2, 1, 3)
print 2 == advance(3, 1, 3)
print 2 == advance(4, 2, 3)
print 1 == advance(5, 2, 3)
print 5 == advance(6, 1, 3)
