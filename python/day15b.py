genA = 883
genB = 879
matchCount = 0

def generateA(genA):
    while True:
        product = genA * 16807
        remainder = product % 2147483647
        if remainder % 4 == 0:
            break
        genA = remainder
    return remainder

def generateB(genB):
    while True:
        product = genB * 48271
        remainder = product % 2147483647
        if remainder % 8 == 0:
            break
        genB = remainder
    return remainder

def getLast16Binary(gen):
    return bin(gen)[2:].zfill(16)[-16:]

for n in range(5000000):

    if n % 10000 == 0:
        print "done "+str(n)

    genA = generateA(genA)
    genB = generateB(genB)
    if getLast16Binary(genA) == getLast16Binary(genB):
        matchCount += 1

print matchCount
