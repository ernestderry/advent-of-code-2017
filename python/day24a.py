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

def largestBridgeStrength(firstComponent, connectedOnPort, components, level):
    firstComponentStrength = getComponentStrength(firstComponent)
    freePort = getFreePortAfterConnection(firstComponent, connectedOnPort)
    largestStrength = firstComponentStrength

    for nextComponent in components:

        if canConnect(freePort, nextComponent):
            remainingComponents = list(components)
            remainingComponents.remove(nextComponent)

            nextComponentBridgeStrength = largestBridgeStrength(nextComponent, freePort, remainingComponents, level + 1)
            candidateLargestBridgeStrength = firstComponentStrength + nextComponentBridgeStrength
            if candidateLargestBridgeStrength > largestStrength:
                largestStrength = candidateLargestBridgeStrength

    return largestStrength

components = []
print largestBridgeStrength("0/1", 0, components, 0) == 1

components = []
print largestBridgeStrength("2/0", 0, components, 0) == 2

components = []
components.append("1/2")
print largestBridgeStrength("1/0", 0, components, 0) == 4

components = []
components.append("1/2")
print largestBridgeStrength("0/1", 0, components, 0) == 4

components = []
components.append("2/2")
print largestBridgeStrength("1/0", 0, components, 0) == 1

components = []
components.append("2/1")
print largestBridgeStrength("0/1", 0, components, 0) == 4

components = []
components.append("2/1")
components.append("3/3")
print largestBridgeStrength("0/1", 0, components, 0) == 4

components = []
components.append("1/2")
components.append("2/3")
components.append("3/4")
print largestBridgeStrength("0/1", 0, components, 0) == 16

components = []
components.append("1/2")
components.append("4/4")
components.append("2/3")
print largestBridgeStrength("0/1", 0, components, 0) == 9

components = []
components.append("1/2")
components.append("2/3")
components.append("2/5")
print largestBridgeStrength("0/1", 0, components, 0) == 11

components = []
components.append("1/2")
components.append("2/5")
components.append("2/3")
print largestBridgeStrength("0/1", 0, components, 0) == 11

components = []
components.append("2/5")
components.append("2/3")
components.append("1/2")
print largestBridgeStrength("0/1", 0, components, 0) == 11

components = []
components.append("0/1")
components.append("2/2")
components.append("2/3")
components.append("3/4")
components.append("3/5")
components.append("10/1")
components.append("9/10")
print largestBridgeStrength("0/1", 0, components, 0) == 31

components = []
components.append("2/5")
components.append("5/2")
components.append("1/2")
print largestBridgeStrength("0/1", 0, components, 0) == 18

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
        print largestBridgeStrength(component, 0, remainingComponents, 0)
