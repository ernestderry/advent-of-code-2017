f = open("c:\\temp\\adcode.txt","r")

registers = {}
highest = 0

def evaluateCondition(comparisonRegister, comparisonSymbol, comparisonInt):
    regValue = int(registers[comparisonRegister])

    if comparisonSymbol == ">":
        return regValue > comparisonInt

    if comparisonSymbol == "<":
        return regValue < comparisonInt

    if comparisonSymbol == ">=":
        return regValue >= comparisonInt

    if comparisonSymbol == "<=":
        return regValue <= comparisonInt

    if comparisonSymbol == "==":
        return regValue == comparisonInt

    if comparisonSymbol == "!=":
        return regValue <> comparisonInt

def performAction(register, action, actionInt):
    global highest
    if action == "inc":
        registers[register] = registers[register] + actionInt
    else:
        registers[register] = registers[register] - actionInt

    if registers[register] > highest:
            highest = registers[register]

def getLargestRegister():
    maxValue = -99999
    for r in registers:
        print r, registers[r]
        if registers[r] > maxValue:
            maxValue = registers[r]
    return maxValue

def processInstructions():
    for line in f:
        lineParts = line.split()
        register = lineParts[0]
        action = lineParts[1]
        actionInt = int(lineParts[2])
        comparisonRegister = lineParts[4]
        comparisonSymbol = lineParts[5]
        comparisonInt = int(lineParts[6])

        if register not in registers:
            registers[register] = 0

        if comparisonRegister not in registers:
            registers[comparisonRegister] = 0

        if evaluateCondition(comparisonRegister, comparisonSymbol, comparisonInt):
            performAction(register, action, actionInt)

processInstructions()
print "highest at the end " + str(getLargestRegister())
print "highest overall " + str(highest)
