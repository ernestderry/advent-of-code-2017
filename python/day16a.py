dancers = []
prevLineUps = []
prevLineUpsLookup = {}

def setUp(inString):
    global dancers
    dancers = list(inString)
    print dancers

def lineUp():
    global dancers
    return reduce(lambda x, y: str(x) + str(y), dancers)

def spin(instruction):
    global dancers
    spinCount = int(instruction[1:]) % len(dancers)
    dancersEnd = dancers[:spinCount*-1]
    dancers = dancers[spinCount*-1:]
    dancers.extend(dancersEnd)

def exchange(instruction):
    global dancers
    ex0 = int(instruction[1:].split("/")[0])
    ex1 = int(instruction[1:].split("/")[1])
    ex0Dancer = dancers[ex0]
    dancers[ex0] = dancers[ex1]
    dancers[ex1] = ex0Dancer

def partner(instruction):
    global dancers
    part0 = instruction[1:].split("/")[0]
    part1 = instruction[1:].split("/")[1]
    part0Pos = dancers.index(part0)
    part1Pos = dancers.index(part1)
    exchange("x"+str(part0Pos)+"/"+str(part1Pos))

setUp("abcde")
print "s1"
spin("s1")
print lineUp() == "eabcd"

print "x3/4"
exchange("x3/4")
print lineUp() == "eabdc"

print "pc/b"
partner("pc/b")
print lineUp() == "eacdb"

print "s4"
spin("s4")
print lineUp() == "acdbe"

print "pe/a"
partner("pe/a")
print lineUp() == "ecdba"

print "x1/3"
exchange("x1/3")
print lineUp() == "ebdca"

print "x4/0"
exchange("x4/0")
print lineUp() == "abdce"

print "x0/4"
exchange("x0/4")
print lineUp() == "ebdca"

print "s2"
spin("s2")
print lineUp() == "caebd"

print "pd/c"
partner("pd/c")
print lineUp() == "daebc"

setUp("abcdefghijklmnop")

lines=[]
f = open("c://temp//adventCode.txt")
for line in f:
    lines.append(line)

    for line in lines:
        for i in line.split(","):
            if i[0:1] == "x":
                exchange(i)
            elif i[0:1] == "s":
                spin(i)
            elif i[0:1] == "p":
                partner(i)
            else:
                print "unknown instruction " + i

print lineUp()
