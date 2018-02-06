def getComponentStrength(component):
    componentPorts = map(int, component.split("/"))
    return componentPorts[0] + componentPorts[1]

def getFreePortAfterConnection(component, connectedOnPort):
    componentPorts = map(int, component.split("/"))
    if componentPorts[0] == connectedOnPort:
        return componentPorts[1]
    elif componentPorts[1] == connectedOnPort:
        return componentPorts[0]
    else:
        return -1

def canConnect(freePort, component):
    componentPorts = map(int, component.split("/"))
    return (componentPorts[0] == freePort or componentPorts[1] == freePort)

def calculateBridgeStrength(bridge):
    components = bridge.split("-")
    strength = 0
    for component in components:
        strength += getComponentStrength(component)

    return strength

def getLongestBridge(bridges):
    longestBridgeLength = 0
    longestBridgeStrength = 0
    longestBridge = ""
    for bridge in bridges:
        bridgeLength = bridge.count("-")
        if bridgeLength > longestBridgeLength:
            longestBridgeLength = bridgeLength
            longestBridge = bridge
            longestBridgeStrength = calculateBridgeStrength(bridge)
        if bridgeLength == longestBridgeLength:
            bridgeStength = calculateBridgeStrength(bridge)
            if bridgeStength > longestBridgeStrength:
                longestBridge = bridge
                longestBridgeStrength = bridgeStength
    return longestBridge

def buildLongestBridge(firstComponent, connectedOnPort, components, level):
    freePort = getFreePortAfterConnection(firstComponent, connectedOnPort)
    candidateBridgesBuilt = []

    for nextComponent in components:
        if canConnect(freePort, nextComponent):
            remainingComponents = list(components)
            remainingComponents.remove(nextComponent)

            nextComponentBridge = buildLongestBridge(nextComponent, freePort, remainingComponents, level + 1)
            candidateBridgesBuilt.append(nextComponentBridge)

    longestBridge = getLongestBridge(candidateBridgesBuilt)

    if longestBridge == "":
        return firstComponent
    else:
        return firstComponent + "-" + longestBridge



components = []
print buildLongestBridge("0/1", 0, components, 0) == "0/1"

components = []
print buildLongestBridge("2/0", 0, components, 0) == "2/0"

components = []
components.append("1/2")
print buildLongestBridge("1/0", 0, components, 0) == "1/0-1/2"

components = []
components.append("1/2")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2"

components = []
components.append("2/2")
print buildLongestBridge("1/0", 0, components, 0) == "1/0"

components = []
components.append("2/1")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-2/1"

components = []
components.append("2/1")
components.append("3/3")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-2/1"

components = []
components.append("1/2")
components.append("2/3")
components.append("3/4")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/3-3/4"

components = []
components.append("1/2")
components.append("4/4")
components.append("2/3")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/3"

components = []
components.append("1/2")
components.append("2/3")
components.append("2/5")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/5"

components = []
components.append("1/2")
components.append("2/5")
components.append("2/3")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/5"

components = []
components.append("2/5")
components.append("2/3")
components.append("1/2")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/5"

components = []
components.append("0/1")
components.append("2/2")
components.append("2/3")
components.append("3/4")
components.append("3/5")
components.append("10/1")
components.append("9/10")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-10/1-9/10"

components = []
components.append("2/5")
components.append("5/2")
components.append("1/2")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/5-5/2"

components = []
components.append("2/5")
components.append("1/99")
components.append("1/2")
print buildLongestBridge("0/1", 0, components, 0) == "0/1-1/2-2/5"

components = []
f = open("c://temp/adcode.txt", "r")
for line in f:
    components.append(line.strip())

for component in components:
    componentPorts = map(int, component.split("/"))
    if componentPorts[0] == 0 or componentPorts[1] == 0:
        print "trying " + str(component)
        remainingComponents = list(components)
        remainingComponents.remove(component)
        longestBridge = buildLongestBridge(component, 0, remainingComponents, 0)
        print "length " + str(longestBridge.count("-"))
        print "strength " + str(calculateBridgeStrength(longestBridge))
