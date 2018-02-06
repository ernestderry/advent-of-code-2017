class InsProcessor:

    def __init__(self, id):
        self.instructions = []
        self.insPos = 0
        self.registers = {}
        self.receivedValues = []
        self.id = id
        self.isWaitingToRecieve = False
        self.registers['p'] = id
        self.sendCount = 0

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

    def setLinkedProcessor(self, insProcessor):
        self.linkedProcessor = insProcessor

    def addToQueue(self, value):
        self.receivedValues.append(value)

    def isWaiting(self):
        return self.isWaitingToRecieve

    def getSendCount(self):
        return self.sendCount

    def processInstruction(self):
        self.isWaitingToRecieve = False
        instruction = self.instructions[self.insPos]

        # print "-------------------------------------------"
        # print "program "+str(self.id)+" doing "+str(instruction)

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
        elif operator == 'add':
            self.registers[operand1] = self.registers[operand1] + self.getValue(operand2)
        elif operator == 'mul':
            self.registers[operand1] = self.registers[operand1] * self.getValue(operand2)
        elif operator == 'mod':
            self.registers[operand1] = self.registers[operand1] % self.getValue(operand2)
        elif operator == 'snd':
            self.linkedProcessor.addToQueue(self.getValue(operand1))
            self.sendCount += 1
        elif operator == 'rcv':
            if len(self.receivedValues) > 0:
                self.registers[operand1] = self.receivedValues[0]
                self.receivedValues = self.receivedValues[1:]
            else:
                self.insPos -= 1
                self.isWaitingToRecieve = True
        elif operator == 'jgz':
            if self.getValue(operand1) > 0:
                self.insPos += (self.getValue(operand2) - 1)

        # print "registers after "+str(self.registers)

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
ip.setRegisters({'a':1})
ip.addInstruction("add a 2")
ip.processInstruction()
print ip.getRegisters()['a'] == 3

ip = InsProcessor(0)
ip.setRegisters({'a':1, 'b':2})
ip.addInstruction("add a b")
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
print ip.getRegisters()['a'] == 8

ip = InsProcessor(0)
ip.setRegisters({'a':7})
ip.addInstruction("mod a 3")
ip.processInstruction()
print ip.getRegisters()['a'] == 1

ip = InsProcessor(0)
ip.setRegisters({'a':7, 'b':3})
ip.addInstruction("mod a b")
ip.processInstruction()
print ip.getRegisters()['a'] == 1

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
ip.addInstruction("jgz a 1")
ip.addInstruction("set a 2")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 2

ip = InsProcessor(0)
ip.setRegisters({'a':1})
ip.addInstruction("jgz a 2")
ip.addInstruction("set a 3")
ip.addInstruction("set b 4")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 1
print ip.getRegisters()['b'] == 4

ip = InsProcessor(0)
ip.setRegisters({'a':0, 'b':0})
ip.addInstruction("jgz a 2")
ip.addInstruction("set a 3")
ip.addInstruction("set b 4")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 3
print ip.getRegisters()['b'] == 0

ip = InsProcessor(0)
ip.setRegisters({'a':-1, 'b':0})
ip.addInstruction("jgz a 2")
ip.addInstruction("set a 3")
ip.addInstruction("set b 4")
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 3
print ip.getRegisters()['b'] == 0

ip = InsProcessor(0)
ip.setRegisters({'a':0})
ip.addInstruction("add a 1")
ip.addInstruction("jgz a -1")
ip.processInstruction()
ip.processInstruction()
ip.processInstruction()
print ip.getRegisters()['a'] == 2

ip = InsProcessor(0)
ip.addInstruction("mul p 17")
ip.processInstruction()
print ip.getRegisters()['p'] == 0

ip1 = InsProcessor(0);
ip2 = InsProcessor(1);
ip1.setLinkedProcessor(ip2)
ip2.setLinkedProcessor(ip1)
ip2.setRegisters({'a':99})
ip2.addInstruction("rcv a")
ip2.processInstruction()
ip2.processInstruction()
ip2.processInstruction()
print ip2.getRegisters()['a'] == 99
print ip2.isWaiting()
ip1.addInstruction("snd 1")
ip1.addInstruction("snd 2")
ip1.addInstruction("snd 3")
ip2.addInstruction("rcv a")
ip2.addInstruction("rcv a")
ip2.addInstruction("rcv a")
ip1.processInstruction()
ip1.processInstruction()
ip1.processInstruction()
ip2.processInstruction()
print ip2.getRegisters()['a'] == 1
ip2.processInstruction()
print ip2.getRegisters()['a'] == 2
ip2.processInstruction()
print ip2.getRegisters()['a'] == 3
print ip2.isWaiting() == False
print ip1.getSendCount() == 3

ip1 = InsProcessor(0)
ip2 = InsProcessor(1)
ip1.setLinkedProcessor(ip2)
ip2.setLinkedProcessor(ip1)
ip1.addInstruction("snd 1")
ip2.addInstruction("snd 1")
ip1.addInstruction("snd 2")
ip2.addInstruction("snd 2")
ip1.addInstruction("snd p")
ip2.addInstruction("snd p")
ip1.addInstruction("rcv a")
ip2.addInstruction("rcv a")
ip2.addInstruction("rcv b")
ip1.addInstruction("rcv b")
ip2.addInstruction("rcv c")
ip1.addInstruction("rcv c")
ip2.addInstruction("rcv d")
ip1.addInstruction("rcv d")

while not (ip1.isWaiting() and ip2.isWaiting()):
    ip1.processInstruction()
    ip2.processInstruction()

print ip1.getSendCount() == 3

ip1 = InsProcessor(0)
ip2 = InsProcessor(1)
ip1.setLinkedProcessor(ip2)
ip2.setLinkedProcessor(ip1)
f = open("c:\\temp\\adcode.txt", "r")
for line in f:
    ip1.addInstruction(line)
    ip2.addInstruction(line)

while not (ip1.isWaiting() and ip2.isWaiting()):
    ip1.processInstruction()
    ip2.processInstruction()

print "answer for processor 1 " + str(ip2.getSendCount())
