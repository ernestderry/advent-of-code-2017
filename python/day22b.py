class Grid:

    def __init__(self, setupString):
        setUpLines = setupString.split("/")
        gridSize = len(setUpLines)
        cornerPoint = gridSize/2
        self.topLeft = []
        self.topLeft.append(cornerPoint * -1)
        self.topLeft.append(cornerPoint * -1)
        self.bottomRight = [cornerPoint, cornerPoint]
        self.currentPos = (0,0)
        self.grid = {}
        self.direction = "Up"
        self.infectionCount = 0

        y = self.topLeft[1]
        for line in setUpLines:
            x = self.topLeft[0]
            for char in line:
                if char == "#":
                    self.grid[(x, y)] = char
                x += 1
            y += 1


    def burst(self):
        if self.currentPos in self.grid:
            status = self.grid[self.currentPos]
            if status == "#":
                self.grid[self.currentPos] = "F"
                self.turnRight()
            elif status == "W":
                self.grid[self.currentPos] = "#"
                self.infectionCount += 1
            else:
                del self.grid[self.currentPos]
                self.turnBack()

            self.move()
        else:
            self.grid[self.currentPos] = "W"
            self.turnLeft()
            self.move()

    def toString(self):
        output = ""
        for y in range(self.topLeft[1], self.bottomRight[1]+1):
            row = ""
            for x in range(self.topLeft[0], self.bottomRight[0]+1):
                if (x, y) in self.grid:
                    char = self.grid[(x, y)]
                else:
                    char = "."
                row += char
            if output == "":
                output = row
            else:
                output += "/" + row
        return output

    def getCurrentPos(self):
        return self.currentPos

    def getInfectionCount(self):
        return self.infectionCount

    def turnLeft(self):
        if self.direction == "Up":
            self.direction = "Left"
        elif self.direction == "Left":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Right"
        else:
            self.direction = "Up"

    def turnBack(self):
        self.turnLeft()
        self.turnLeft()

    def turnRight(self):
        self.turnLeft()
        self.turnLeft()
        self.turnLeft()

    def move(self):
        if self.direction == "Up":
            self.currentPos = (self.currentPos[0], self.currentPos[1] - 1)
        elif self.direction == "Left":
            self.currentPos = (self.currentPos[0] - 1, self.currentPos[1])
        elif self.direction == "Down":
            self.currentPos = (self.currentPos[0], self.currentPos[1] + 1)
        elif self.direction == "Right":
            self.currentPos = (self.currentPos[0] + 1, self.currentPos[1])

        if self.currentPos[0] < self.topLeft[0]:
            self.topLeft[0] = self.currentPos[0]

        if self.currentPos[1] < self.topLeft[1]:
            self.topLeft[1] = self.currentPos[1]

        if self.currentPos[0] > self.bottomRight[0]:
            self.bottomRight[0] = self.currentPos[0]

        if self.currentPos[1] > self.bottomRight[1]:
            self.bottomRight[1] = self.currentPos[1]

    def getDirection(self):
        return self.direction


grid = Grid("..#/#../...")
grid.burst()
print grid.toString() == "..#/#W./..."
print grid.getCurrentPos() == (-1, 0)
print grid.getDirection() == "Left"

grid.burst()
print grid.toString() == "..#/FW./..."
print grid.getCurrentPos() == (-1, -1)
print grid.getDirection() == "Up"

grid.burst()
grid.burst()
grid.burst()
print grid.toString() == "WW.#/WFW./...."
print grid.getCurrentPos() == (-1, 0)
print grid.getDirection() == "Right"

grid.burst()
print grid.toString() == "WW.#/W.W./...."
print grid.getCurrentPos() == (-2, 0)
print grid.getDirection() == "Left"

grid.burst()
print grid.toString() == ".WW.#/.#.W./....."
print grid.getCurrentPos() == (-3, 0)
print grid.getDirection() == "Left"

#longer test
grid = Grid("..#/#../...")
for n in range(100):
    grid.burst()
print grid.getInfectionCount() == 26

#longer test2
# grid = Grid("..#/#../...")
# for n in range(10000000):
#     grid.burst()
#     if n % 100000 == 0:
#         print "done "+str(n)
# print grid.getInfectionCount() = 2511944

#solve problem
f = open("c://temp/adcode.txt", "r")
gridString = ""
for line in f:
    if gridString == "":
        gridString = line.strip()
    else:
        gridString += "/"+line.strip()
grid = Grid(gridString)
for n in range(10000000):
    grid.burst()
    if n % 100000 == 0:
        print "done "+str(n)
print "answer "+str(grid.getInfectionCount())
