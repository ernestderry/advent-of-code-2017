graph = {}
programs = []

def addProgramToGraph(line):
    lineparts = line.replace(",", "").split()
    program = lineparts[0]
    programs.append(program)
    connections = lineparts[2:]
    graph[program] = connections

def findGroup(group, program):
    if program not in group:
        group.append(program)
        print "adding "+program
        programs.remove(program)
        directConnections = graph[program]
        for connection in directConnections:
            findGroup(group, connection)

f = open("C:\\temp\\adcode.txt", "r")
for line in f:
    addProgramToGraph(line)

print graph

groupCount = 0
while len(programs) > 0:
    groupCount += 1
    program = programs[0]

    print "searching for group containing "+program
    group = []
    findGroup(group, program)
    print "group contains "+str(len(group))+" programs"

print "number of groups " + str(groupCount)
