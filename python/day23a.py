class InsProcessor:
    def __init__(self, id):
        self.instructions = []
        self.insPos = 0
        self.registers = {}
        self.id = id
        self.mulCount = 0

    def getValue(self, operand):
        if operand[0].isalpha():
            opValue = int(self.registers[operand])
        else:
            opValue = int(operand)
        return opValue

    def checkOperand(self, operand):
        if operand[0].isalpha() and operand not in self.registers:
            self.registers[operand] = 0

    def addInstruction(self, instruction):
        self.instructions.append(instruction)

    def getRegisters(self):
        return self.registers

    def setRegisters(self, registers):
        self.registers = registers

    def getMulCount(self):
        return self.mulCount

    def processInstruction(self):
        self.isWaitingToRecieve = False
        instruction = self.instructions[self.insPos]
        print "program "+str(self.id)+" doing "+str(instruction)
        instructionParts = instruction.split()
        operator = instructionParts[0]
        operand1 = instructionParts[1]
        self.checkOperand(operand1)
        self.insPos += 1
        if len(instructionParts) > 2:
            operand2 = instructionParts[2]
            self.checkOperand(operand2)
        if operator == 'set':
            self.registers[operand1] = self.getValue(operand2)
        elif operator == 'sub':
            self.registers[operand1] = self.registers[operand1] - self.getValue(operand2)
        elif operator == 'mul':
            self.registers[operand1] = self.registers[operand1] * self.getValue(operand2)
            self.mulCount += 1
        elif operator == 'jnz':
            if self.getValue(operand1) <> 0:
                self.insPos += (self.getValue(operand2) - 1)

    def finished(self):
        return self.insPos > (len(self.instructions) - 1)

ip = InsProcessor(0)
ip.addInstruction("set a 1")
ip.processInstruction()
print ip.getRegisters()['a'] == 1

ip = InsProcessor(0)
ip.setRegisters({'a':1})
ip.addInstruction("set a 2")
ip.processInstruction()
print ip.getRegisters()['a'] == 2

ip = InsProcessor(0)
ip.setRegisters({'a':1})
ip.addInstruction("set b a")
ip.processInstruction()
print ip.getRegisters()['b'] == 1

ip = InsProcessor(0)
ip.setRegisters({'a':3})
ip.addInstruction("sub a 2")
ip.processInstruction()
print ip.getRegisters()['a'] == 1

ip = InsProcessor(0)
ip.setRegisters({'a':5, 'b':2})
ip.addInstruction("sub a b")
ip.processInstruction()
print ip.getRegisters()['a'] == 3

ip = InsProcessor(0)
ip.setRegisters({'a':2})
ip.addInstruction("mul a 3")
ip.processInstruction()

print ip.getRegisters()['a'] == 6
ip = InsProcessor(0)
ip.setRegisters({'a':2, 'b':4})
ip.addInstruction("mul a b")
ip.processInstruction()

ip = InsProcessor(0)
ip.addInstruction("set a 1")
ip.addInstruction("set a 4")
ip.addInstruction("set a 6")
ip.processInstruction()
print 1 ==ip.getRegisters()['a']
ip.processInstruction()
print 4 ==ip.getRegisters()['a']
ip.processInstruction()
print 6 ==ip.getRegisters()['a']

ip = InsProcessor(0)
ip.setRegisters({'a':1})
ip.addInstruction("jnz a 1")
ip.addInstruction("set a 2")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 2

ip = InsProcessor(0)
ip.setRegisters({'a':1})
ip.addInstruction("jnz a 2")
ip.addInstruction("set a 3")
ip.addInstruction("set b 4")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 1
print ip.getRegisters()['b'] == 4

ip = InsProcessor(0)
ip.setRegisters({'a':0, 'b':0})
ip.addInstruction("jnz a 2")
ip.addInstruction("set a 3")
ip.addInstruction("set b 4")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 3
print ip.getRegisters()['b'] == 0

ip = InsProcessor(0)
ip.setRegisters({'a':-1, 'b':0})
ip.addInstruction("jnz a 2")
ip.addInstruction("set a 3")
ip.addInstruction("set b 4")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == -1
print ip.getRegisters()['b'] == 4

ip = InsProcessor(0)
ip.setRegisters({'a':10})
ip.addInstruction("sub a 1")
ip.addInstruction("jnz a -1")
ip.processInstruction()
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 8

ip = InsProcessor(0)
ip.addInstruction("mul p 17")
ip.processInstruction()
print ip.getRegisters()['p'] == 0

ip = InsProcessor(0)
f = open("c://temp/adcode.txt", "r")
for line in f:
    ip.addInstruction(line.strip())

while not ip.finished():
    ip.processInstruction()

print ip.getMulCount()
