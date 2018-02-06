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
            #not allowed to move diagonally in our 2D hex grid representation, only move left
            x -= 1
        elif x < 0 and y < 0:
            #not allowed to move diagonally in our 2D hex grid representation, only move right
            x += 1

    return stepCount

def findFurthestDistanceAtAnyPointInHexGrid(instructionsString):
    instructions = instructionsString.split(",")
    x = 0
    y = 0
    furthestDistanceInSteps = 0

    for step in instructions:
        #take hex grid direction steps across a 2D representation of a hex grid
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

        distanceAway = getDistanceInSteps(x, y)
        if distanceAway > furthestDistanceInSteps:
            furthestDistanceInSteps = distanceAway

    return furthestDistanceInSteps

f = open("c:\\temp\\adcode.txt","r")
for line in f:
    print findFurthestDistanceAtAnyPointInHexGrid(line)
