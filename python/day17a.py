def advance(slock, startPos, steps):
    slockLen = len(slock)
    stepsAfterFullRotations = steps % slockLen

    newPos = startPos + stepsAfterFullRotations
    if newPos > (slockLen - 1):
        newPos -= slockLen

    return newPos

spinLock = [0]
currentPos = 0
for n in range(1, 2018):
    newPos = advance(spinLock, currentPos, 345)
    spinLock.insert(newPos+1, n)
    currentPos = newPos+1

print "answer " + str(spinLock[currentPos+1])


print
print "testing"
print 0 == advance([0], 0, 1)
print 0 == advance([0], 0, 4)
print 1 == advance([0, 1], 0, 1)
print 1 == advance([0, 1], 1, 2)
print 1 == advance([0, 1], 0, 3)
print 0 == advance([0, 1], 1, 3)
print 1 == advance([0, 1, 2, 3], 2, 7)
