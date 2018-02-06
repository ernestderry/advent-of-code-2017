#slow but gets there in the end

import copy
firewall = {}
saveFirewall = {}

class Scanner:
    scannerRange = 0
    direction = 1
    scannerPos = 1


    def __init__(self, scannerRange):
        self.scannerRange = scannerRange

    def getRange(self):
        return self.scannerRange

    def getDirection(self):
        return self.direction

    def getScannerPos(self):
        return self.scannerPos

    def resetScanner(self):
        self.scannerPos = 1
        self.diretion = 1

    def moveScanner(self):
        self.scannerPos += self.direction
        if self.scannerPos > self.scannerRange or self.scannerPos < 1:
                self.direction = self.direction * -1
                self.scannerPos += (self.direction * 2)

def moveScanners():
    for layer in firewall:
        firewall[layer].moveScanner()

def saveScanners():
    global saveFirewall
    saveFirewall = copy.deepcopy(firewall)

def resetScanners():
    global firewall
    firewall = copy.deepcopy(saveFirewall)

f = open("c:\\temp\\adcode.txt")
for line in f:
    lineParts = line.split(":")
    depth = int(lineParts[0])
    scannerRange = int(lineParts[1])

    scanner = Scanner(scannerRange)
    firewall[depth] = scanner

saveScanners()
firewallDepth = depth

escaped = False
delay = -1
while not escaped:
    escaped = True
    delay += 1

    if delay % 100 == 0:
        print "trying delay "+str(delay)

    resetScanners()

    firstTime = True
    for packetLayer in range(-1, firewallDepth+1):
        packetLayer += 1

        if packetLayer in firewall:
            scanner = firewall[packetLayer]
            if scanner.getScannerPos() == 1:
                escaped = False

        moveScanners()
        if firstTime == True:
            saveScanners()
            firstTime = False

        if not escaped:
            break

print "Escaped with delay time of " + str(delay)
