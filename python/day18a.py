sound = 0
instructions = []
insPos = 0
registers = {}
recover = False

def getValue(operand):
    if operand[0].isalpha():
        opValue = int(registers[operand])
    else:
        opValue = int(operand)
    return opValue

def checkOperand(operand):
    global registers
    if operand not in registers:
        registers[operand] = 0

def processInstruction():
    global sound, registers, insPos, instructions, recover
    instruction = instructions[insPos]
    instructionParts = instruction.split()
    operator = instructionParts[0]
    operand1 = instructionParts[1]
    checkOperand(operand1)

    insPos += 1

    if len(instructionParts) > 2:
        operand2 = instructionParts[2]
        checkOperand(operand2)

    if operator == 'set':
        registers[operand1] = getValue(operand2)
    elif operator == 'add':
        registers[operand1] = registers[operand1] + getValue(operand2)
    elif operator == 'mul':
        registers[operand1] = registers[operand1] * getValue(operand2)
    elif operator == 'mod':
        registers[operand1] = registers[operand1] % getValue(operand2)
    elif operator == 'snd':
        sound = getValue(operand1)
    elif operator == 'rcv':
        if getValue(operand1) <> 0:
            recover = True
    elif operator == 'jgz':
        if getValue(operand1) > 0:
            insPos += (getValue(operand2) - 1)


def testSetup():
    global registers, insPos, instructions, sound, recover
    registers = {}
    insPos = 0
    instructions = []
    sound = 0
    recover = False

testSetup()
instructions.append("set a 1")
processInstruction()
print registers['a'] == 1

testSetup()
registers = {'a':1}
instructions.append("set a 2")
processInstruction()
print registers['a'] == 2

testSetup()
registers = {'a':1}
instructions.append("set b a")
processInstruction()
print registers['b'] == 1

testSetup()
registers = {'a':1}
instructions.append("add a 2")
processInstruction()
print registers['a'] == 3

testSetup()
registers = {'a':1, 'b':2}
instructions.append("add a b")
processInstruction()
print registers['a'] == 3

testSetup()
registers = {'a':2}
instructions.append("mul a 3")
processInstruction()
print registers['a'] == 6

testSetup()
registers = {'a':2, 'b':4}
instructions.append("mul a b")
processInstruction()
print registers['a'] == 8

testSetup()
registers = {'a':7}
instructions.append("mod a 3")
processInstruction()
print registers['a'] == 1

testSetup()
registers = {'a':7, 'b':3}
instructions.append("mod a b")
processInstruction()
print registers['a'] == 1

testSetup()
registers = {}
instructions.append("snd 1")
processInstruction()
print sound == 1

testSetup()
registers = {'a':3}
instructions.append("snd a")
processInstruction()
print sound == 3

testSetup()
registers = {'a':0}
instructions.append("rcv a")
processInstruction()
print recover == False


testSetup()
registers = {'a':1}
instructions.append("rcv a")
processInstruction()
print recover == True

testSetup()
registers = {'a':-1}
instructions.append("rcv a")
processInstruction()
print recover == True

testSetup()
instructions.append("set a 1")
instructions.append("set a 4")
instructions.append("set a 6")
processInstruction()
processInstruction()
processInstruction()
print 6 == registers['a']
print insPos == 3

testSetup()
registers = {'a':1}
instructions.append("jgz a 1")
processInstruction()
print insPos == 1

testSetup()
registers = {'a':1}
instructions.append("jgz a 2")
processInstruction()
print insPos == 2

testSetup()
registers = {'a':0}
instructions.append("jgz a 2")
processInstruction()
print insPos == 1

testSetup()
registers = {'a':-1}
instructions.append("jgz a 2")
processInstruction()
print insPos == 1

testSetup()
instructions.append("set a 1")
instructions.append("jgz a -1")
processInstruction()
processInstruction()
print insPos == 0

testSetup()
instructions.append("mul p 17")
processInstruction()
print registers['p'] == 0

testSetup()
instructions.append("set a 1")
instructions.append("add a 2")
instructions.append("mul a a")
instructions.append("mod a 5")
instructions.append("snd a")
instructions.append("set a 0")
instructions.append("rcv a")
instructions.append("jgz a -1")
instructions.append("set a 1")
instructions.append("jgz a -2")
while recover == False:
    processInstruction()
print sound == 4

testSetup()
f = open("c:\\temp\\adcode.txt", "r")
for line in f:
    instructions.append(line)

while recover == False:
    processInstruction()
print "answer " + str(sound)
