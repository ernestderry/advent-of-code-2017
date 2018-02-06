graph = {}

def addProgramToGraph(line):
    lineparts = line.replace(",", "").split()
    program = lineparts[0]
    connections = lineparts[2:]
    graph[program] = connections

def findGroup(group, program):
    if program not in group:
        group.append(program)
        print "adding "+program
        directConnections = graph[program]
        for connection in directConnections:
            findGroup(group, connection)

f = open("C:\\temp\\adcode.txt", "r")
for line in f:
    addProgramToGraph(line)

print graph
group = []
print findGroup(group, "0")
print "group " + str(group)
print "length " + str(len(group))
