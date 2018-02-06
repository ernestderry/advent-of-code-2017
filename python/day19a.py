def canGoRight(cells, x, y):
    rightChar = cells[(x+1, y)]
    return (rightChar == "-" or rightChar.isalpha())

def canGoDown(cells, x, y):
    downChar = cells[(x, y-1)]
    return (downChar == "|" or downChar.isalpha())

def canGoUp(cells, x, y):
    upChar = cells[(x, y+1)]
    return (upChar == "|" or upChar.isalpha())

def goingLeft(direction):
    return direction == 4

def traceRoute(paths):
    cells = {}
    collectedLetters = ""
    direction = 3
    y = 0
    for line in paths:
        x = 0
        for char in line:
            cellData = char
            cells[(x, y)] = cellData
            x += 1
        y += 1

    finished = False
    y = 0
    x = paths[0].index("|")
    while not finished:
        if direction == 3:
            y += 1
        elif direction == 2:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 4:
            x -= 1

        cellData = cells[(x, y)]
        if cellData.isalpha():
            collectedLetters += cellData

        if cellData == "+":
            if canGoRight(cells, x, y) and direction <> 4:
                direction = 2
            elif canGoDown(cells, x, y) and direction <> 3:
                direction = 1
            elif canGoUp(cells, x, y) and direction <> 1:
                direction = 3
            else:
                direction = 4

        finished = (cellData == "U")

    return collectedLetters

paths = []
paths.append(" | ")
paths.append(" U ")
paths.append("   ")
print "U" == traceRoute(paths)

paths = []
paths.append(" | ")
paths.append(" A ")
paths.append(" | ")
paths.append(" | ")
paths.append(" X ")
paths.append(" | ")
paths.append(" U ")
paths.append("   ")
print "AXU" == traceRoute(paths)

paths = []
paths.append(" |   ")
paths.append(" +-U ")
paths.append("     ")
print "U" == traceRoute(paths)

paths = []
paths.append(" |       ")
paths.append(" B       ")
paths.append(" |       ")
paths.append(" +-A---U ")
paths.append("         ")
print "BAU" == traceRoute(paths)

paths = []
paths.append(" |   ")
paths.append(" +-U ")
paths.append("     ")
print "U" == traceRoute(paths)

paths = []
paths.append(" |          ")
paths.append(" +-A-+      ")
paths.append("     |      ")
paths.append("     X      ")
paths.append("     |      ")
paths.append("     +----U ")
paths.append("            ")
print "AXU" == traceRoute(paths)

paths = []
paths.append(" |   U ")
paths.append(" |   | ")
paths.append(" +-A-+ ")
paths.append("       ")
print "AU" == traceRoute(paths)

paths = []
paths.append("      | ")
paths.append("      E ")
paths.append("      | ")
paths.append("      U ")
paths.append("        ")
print "EU" == traceRoute(paths)

paths = []
paths.append("      | ")
paths.append("  U-F-+ ")
paths.append("        ")
print "FU" == traceRoute(paths)

paths = []
paths.append("    U | ")
paths.append("    | | ")
paths.append("    +-+ ")
paths.append("        ")
print "U" == traceRoute(paths)

paths = []
paths.append("      | ")
paths.append("  U-+ | ")
paths.append("    | | ")
paths.append("    +-+ ")
paths.append("        ")
print "U" == traceRoute(paths)

paths = []
paths.append("           | ")
paths.append(" +-S-----+ C ")
paths.append(" |       | | ")
paths.append(" |       E | ")
paths.append(" |       | | ")
paths.append(" E  U----+ H ")
paths.append(" |         |")
paths.append(" +------E--+ ")
paths.append("             ")
print "CHEESEU" == traceRoute(paths)

paths = []
paths.append("           | ")
paths.append(" +S------+ C ")
paths.append(" |       E | ")
paths.append(" |       | | ")
paths.append(" |       | | ")
paths.append(" |      U+ | ")
paths.append(" E         H")
paths.append(" +--------E+ ")
paths.append("             ")
print "CHEESEU" == traceRoute(paths)

paths = []
paths.append("           |    ")
paths.append("        U  H    ")
paths.append("        |  |    ")
paths.append(" +--L------|--+ ")
paths.append(" |      O  |  | ")
paths.append(" |      |  |  | ")
paths.append(" |      +--|L-+ " )
paths.append(" |         |    ")
paths.append(" +--------E+    ")
paths.append("                ")
print "HELLOU" == traceRoute(paths)


paths = []
f = open("c://temp/adcode.txt", "r")
for line in f:
    paths.append(line)

print traceRoute(paths)
