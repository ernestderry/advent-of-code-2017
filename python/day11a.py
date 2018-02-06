def getDistanceInSteps(x, y):
    stepCount = 0
    while x <> 0 or y <> 0:
        stepCount +=1
        if x < 0 and y > 0:
            x += 1
            y -= 1
        elif x > 0 and y < 0:
            x -= 1
            y += 1
        elif x == 0 and y < 0:
            y += 1
        elif x == 0 and y > 0:
            y -= 1
        elif x > 0 and y == 0:
            x -= 1
        elif x < 0 and y == 0:
            x += 1
        elif x > 0 and y > 0:
            x -= 1
        elif x < 0 and y < 0:
            x += 1

    return stepCount

def findStepsAway(instructionsString):
    instructions = instructionsString.split(",")
    x = 0
    y = 0
    for step in instructions:
        if step == 'n':
            y += 1
        elif step == 's':
            y -= 1
        elif step == 'ne':
            x += 1
        elif step == 'nw':
            x -= 1
            y += 1
        elif step == 'se':
            x += 1
            y -= 1
        elif step == 'sw':
            x -= 1

    print "x " + str(x)
    print "y " + str(y)

    return getDistanceInSteps(x, y)

f = open("c:\\temp\\adcode.txt","r")
for line in f:
    print findStepsAway(line)
