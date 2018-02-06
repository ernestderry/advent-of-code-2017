tree = {}
highestProgramWithProblem = ""

def buildTree():
    f = open("c:\\temp\\adcode.txt","r")
    for line in f:
        lineParts = line.replace(",", "").split()
        program = lineParts[0]
        weight = int(lineParts[1].replace("(","").replace(")",""))
        children = list(lineParts[3:])

        node = []
        node.append("")
        node.append(weight)
        node.append(children)
        node.append(0)

        tree[program] = node

    #set parents
    for t in tree:
        node = tree[t]
        for child in node[2]:
            tree[child][0] = t


def setTowerWeights(program):
    towerWeight = 0
    for child in tree[program][2]:
        childTowerWeight = setTowerWeights(child)
        tree[child][3] = childTowerWeight
        towerWeight += childTowerWeight

    towerWeight += tree[program][1]
    return towerWeight

def findUnbalancedProgram(program):
    print "checking "+program
    childWeights = []
    childNames = []
    for child in tree[program][2]:
        findUnbalancedProgram(child)

        childWeights.append(tree[child][3])
        childNames.append(child)

    if len(childWeights) > 1 :
        firstWeight = childWeights[0]
        for weightIdx in range(1, len(childWeights)):
            if childWeights[weightIdx] <> firstWeight:
                print "Problem with program " + program
                print "Weights " + str(childWeights)
                print "Children " + str(childNames)


                

buildTree()
print tree
for t in tree:
    if tree[t][0] == "":
        bottomProgram = t
print "bottomProgram " + bottomProgram

setTowerWeights(bottomProgram)
print tree

findUnbalancedProgram(bottomProgram)

#After reviewing output of programs with a problem. I took the first one (highest)
#and could see that one of the children 'gozhrsf' was out by 5. 'gozhrsf's original
#weight was 762, so reducing it to 757 would balance the tree
