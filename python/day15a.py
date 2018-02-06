genA = 883
genB = 879
matchCount = 0

def generateA(genA):
    product = genA * 16807
    remainder = product % 2147483647
    return remainder

def generateB(genB):
    product = genB * 48271
    remainder = product % 2147483647
    return remainder

def getLast16Binary(gen):
    return bin(gen)[2:].zfill(16)[-16:]

for n in range(40000000):

    if n % 100000 == 0:
        print "done "+str(n)

    genA = generateA(genA)
    genB = generateB(genB)

    if getLast16Binary(genA) == getLast16Binary(genB):
        matchCount += 1

print matchCount
