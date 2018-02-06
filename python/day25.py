
rules = {}
tape = {}

def extractStateRule():
    line = f.readline().strip()
    ruleValue = int(line.split(" ")[5][0:1])
    line = f.readline().strip()
    ruleNewValue = int(line.split(" ")[4][0:1])
    line = f.readline().strip()
    direction = line.split(" ")[6][0:-1]
    if direction == "left":
        ruleDirection = -1
    else:
        ruleDirection = 1
    line = f.readline().strip()
    ruleNewState = line.split(" ")[4][0:1]

    rules[(ruleState, ruleValue)] = (ruleNewValue, ruleDirection, ruleNewState)

def getTapeValue(pos):
    if pos in tape:
        return tape[pos]
    else:
        tape[pos] = 0
        return 0

f = open("c://temp/adcode.txt", "r")
while True:
    line = f.readline()
    if line == "":
        break
    line = line.strip()
    if line[0:14] == "Begin in state":
        currentState = line.split(" ")[3][0:1]

    if line[0:7] == "Perform":
        runSteps = int(line.split(" ")[5])

    if line[0:8] == "In state":
        ruleState = line.split(" ")[2][0:1]

        extractStateRule()
        extractStateRule()

currentPos = 0
for n in range(runSteps):
    newStateData = rules[(currentState, getTapeValue(currentPos))]
    tape[currentPos] = newStateData[0]
    currentPos += newStateData[1]
    currentState = newStateData[2]

counter = 0
for slot in tape:
    if tape[slot] == 1:
        counter += 1

print "answer " + str(counter)
