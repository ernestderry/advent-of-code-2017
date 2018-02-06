tree = {}
def buildTree():
    f = open("c:\\temp\\adcode.txt","r")
    for line in f:
        lineParts = line.replace(",", "").split()
        program = lineParts[0]
        weight = lineParts[1]
        children = list(lineParts[3:])

        node = []
        node.append("")
        node.append(weight)
        node.append(children)

        tree[program] = node

    #set parents
    for t in tree:
        node = tree[t]
        for child in node[2]:
            tree[child][0] = t



buildTree()
print tree
print "answer"
for t in tree:
    if tree[t][0] == "":
        print t
