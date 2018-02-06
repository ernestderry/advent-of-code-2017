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
        self.grid = set()
        self.direction = "Up"
        self.infectionCount = 0

        y = self.topLeft[1]
        for line in setUpLines:
            x = self.topLeft[0]
            for char in line:
                if char == "#":
                    self.grid.add((x, y))
                x += 1
            y += 1


    def burst(self):
        if self.currentPos in self.grid:
            self.grid.remove(self.currentPos)
            self.turnRight()
            self.move()
        else:
            self.grid.add(self.currentPos)
            self.turnLeft()
            self.move()
            self.infectionCount += 1

    def toString(self):
        output = ""
        for y in range(self.topLeft[1], self.bottomRight[1]+1):
            row = ""
            for x in range(self.topLeft[0], self.bottomRight[0]+1):
                if (x, y) in self.grid:
                    char = "#"
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

    def turnRight(self):
        if self.direction == "Up":
            self.direction = "Right"
        elif self.direction == "Left":
            self.direction = "Up"
        elif self.direction == "Down":
            self.direction = "Left"
        else:
            self.direction = "Down"

    def turnLeft(self):
        if self.direction == "Up":
            self.direction = "Left"
        elif self.direction == "Left":
            self.direction = "Down"
        elif self.direction == "Down":
            self.direction = "Right"
        else:
            self.direction = "Up"

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



#not infected, move Left
grid = Grid("..#/#../...")
grid.burst()
print grid.toString() == "..#/##./..."
print grid.getCurrentPos() == (-1, 0)
print grid.getDirection() == "Left"

#infected, move right
grid.burst()
print grid.toString() == "..#/.#./..."
print grid.getCurrentPos() == (-1, -1)
print grid.getDirection() == "Up"

#extend grid
grid.burst()
print grid.toString() == ".#.#/..#./...."
print grid.getCurrentPos() == (-2, -1)
print grid.getDirection() == "Left"

grid.burst()
print grid.toString() == "##.#/..#./...."
print grid.getCurrentPos() == (-2, 0)
print grid.getDirection() == "Down"

grid.burst()
print grid.toString() == "##.#/#.#./...."
print grid.getCurrentPos() == (-1, 0)
print grid.getDirection() == "Right"

grid.burst()
print grid.toString() == "##.#/###./...."
print grid.getCurrentPos() == (-1, -1)
print grid.getDirection() == "Up"

grid.burst()
print grid.toString() == "#..#/###./...."
print grid.getCurrentPos() == (0, -1)
print grid.getDirection() == "Right"

#70 burst test
grid = Grid("..#/#../...")
for n in range(70):
    grid.burst()
print grid.toString() == "...##../..#..#./.#....#/#.#...#/#.#..#./...##.."
print grid.getCurrentPos() == (1, -1)
print grid.getDirection() == "Up"
print grid.getInfectionCount() == 41

#10000 burst test
grid = Grid("..#/#../...")
for n in range(10000):
    grid.burst()
print grid.getInfectionCount() == 5587

#solve problem
f = open("c://temp/adcode.txt", "r")
gridString = ""
for line in f:
    if gridString == "":
        gridString = line.strip()
    else:
        gridString += "/"+line.strip()
grid = Grid(gridString)
for n in range(10000):
    grid.burst()
print "answer "+str(grid.getInfectionCount())
