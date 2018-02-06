def buildGridOfZeros():
    grid = []
    for i in range(999):
        rowList = []
        for i in range(999):
            rowList.append(0)
        grid.append(rowList)
    return grid

def getCellValue(grid, x, y):
    total = 0
    total += grid[x+1][y]
    total += grid[x+1][y+1]
    total += grid[x][y+1]
    total += grid[x-1][y+1]
    total += grid[x-1][y]
    total += grid[x-1][y-1]
    total += grid[x][y-1]
    total += grid[x+1][y-1]
    return total

def getGridValue(num):
    grid = buildGridOfZeros()
    x = 500
    y = 500
    direction = 1
    turnAfterSteps = 1
    sidesOfCurrentSteps = 0
    steps = 0
    grid[x][y] = 1

    while num > 1:
        if direction == 1:
            x += 1
        if direction == 2:
            y += 1
        if direction == 3:
            x -= 1
        if direction == 4:
            y -= 1

        grid[x][y] = getCellValue(grid, x, y)

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

    return grid[x][y]

i = 1
while True:
    i += 1
    cellValue = getGridValue(i)
    print cellValue
    if cellValue > 277678:
        print cellValue
        break

print "1 - " + str(getGridValue(1) == 1)
print "2 - " + str(getGridValue(2) == 1)
print "3 - " + str(getGridValue(3) == 2)
print "4 - " + str(getGridValue(4) == 4)
print "5 - " + str(getGridValue(5) == 5)
print "6 - " + str(getGridValue(6) == 10)
print "7 - " + str(getGridValue(7) == 11)
print "8 - " + str(getGridValue(8) == 23)
print "17 - " + str(getGridValue(17) == 147)
print "23 - " + str(getGridValue(23) == 806)
