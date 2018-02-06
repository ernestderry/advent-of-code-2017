firewall = {}

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

    def moveScanner(self):
        self.scannerPos += self.direction
        if self.scannerPos > self.scannerRange or self.scannerPos < 1:
                self.direction = self.direction * -1
                self.scannerPos += (self.direction * 2)

def moveScanners():
    for layer in firewall:
        firewall[layer].moveScanner()

f = open("c:\\temp\\adcode.txt")
for line in f:
    lineParts = line.split(":")
    depth = int(lineParts[0])
    scannerRange = int(lineParts[1])

    scanner = Scanner(scannerRange)
    firewall[depth] = scanner

firewallDepth = depth

severity = 0
for packetLayer in range(-1, firewallDepth+1):
    packetLayer += 1

    if packetLayer in firewall:
        scanner = firewall[packetLayer]
        if scanner.getScannerPos() == 1:
            severity = severity + (packetLayer * scanner.getRange())

    moveScanners()

print "answer " + str(severity)
