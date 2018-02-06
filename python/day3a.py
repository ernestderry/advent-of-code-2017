def getGridRef(num):
    x = 0
    y = 0
    direction = 1
    turnAfterSteps = 1
    sidesOfCurrentSteps = 0
    steps = 0
    while num > 1:
        if direction == 1:
            x += 1
        if direction == 2:
            y += 1
        if direction == 3:
            x -= 1
        if direction == 4:
            y -= 1

        steps += 1
        if steps == turnAfterSteps:
            steps = 0
            direction += 1
            if direction == 5:
                direction = 1
            sidesOfCurrentSteps += 1
            if sidesOfCurrentSteps == 2:
                sidesOfCurrentSteps = 0
                turnAfterSteps += 1
        num -= 1

    return (x, y)

gridRef = getGridRef(277678)
print gridRef
print "answer = "+str(abs(gridRef[0]) + abs(gridRef[1]))

print "1 - " + str(getGridRef(1)[0] == 0 and getGridRef(1)[1] == 0)
print "2 - " + str(getGridRef(2)[0] == 1 and getGridRef(2)[1] == 0)
print "3 - " + str(getGridRef(3)[0] == 1 and getGridRef(3)[1] == 1)
print "4 - " + str(getGridRef(4)[0] == 0 and getGridRef(4)[1] == 1)
print "5 - " + str(getGridRef(5)[0] == -1 and getGridRef(5)[1] == 1)
print "6 - " + str(getGridRef(6)[0] == -1 and getGridRef(6)[1] == 0)
print "7 - " + str(getGridRef(7)[0] == -1 and getGridRef(7)[1] == -1)
print "8 - " + str(getGridRef(8)[0] == 0 and getGridRef(8)[1] == -1)
print "9 - " + str(getGridRef(9)[0] == 1 and getGridRef(9)[1] == -1)
print "10 - " + str(getGridRef(10)[0] == 2 and getGridRef(10)[1] == -1)
print "13 - " + str(getGridRef(13)[0] == 2 and getGridRef(13)[1] == 2)
print "17 - " + str(getGridRef(17)[0] == -2 and getGridRef(17)[1] == 2)
print "21 - " + str(getGridRef(21)[0] == -2 and getGridRef(21)[1] == -2)
print "26 - " + str(getGridRef(26)[0] == 3 and getGridRef(26)[1] == -2)
