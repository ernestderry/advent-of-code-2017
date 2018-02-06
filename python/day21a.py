def convertListToString(listOfStrings):
    combinedString = ""
    for line in listOfStrings:
        if combinedString == "":
            combinedString = line
        else:
            combinedString += ("/" + line)
    return combinedString

def flipVertical(pattern):
    return convertListToString(pattern.split("/")[::-1])

def flipHorizontal(pattern):
    return convertListToString(map(lambda x:x[::-1], pattern.split("/")))

def rotateRight(pattern):
    patternBits = pattern.split("/")
    if len(patternBits) == 3:
        line0 = patternBits[2][0] + patternBits[1][0] + patternBits[0][0]
        line1 = patternBits[2][1] + patternBits[1][1] + patternBits[0][1]
        line2 = patternBits[2][2] + patternBits[1][2] + patternBits[0][2]
        return line0 + "/" + line1 + "/" + line2
    else:
        line0 = patternBits[1][0] + patternBits[0][0]
        line1 = patternBits[1][1] + patternBits[0][1]
        return line0 + "/" + line1

def size3Pattern(pattern):
    return pattern.count("/") == 2

def patternMatch(pattern, rulePattern):
    if pattern == rulePattern:
        return True
    if flipVertical(pattern) == rulePattern:
        return True
    if flipHorizontal(pattern) == rulePattern:
        return True
    if flipHorizontal(flipVertical(pattern)) == rulePattern:
        return True
    if rotateRight(pattern) == rulePattern:
        return True
    if flipVertical(rotateRight(pattern)) == rulePattern:
        return True
    if flipHorizontal(rotateRight(pattern)) == rulePattern:
        return True
    if flipHorizontal(flipVertical(rotateRight(pattern))) == rulePattern:
        return True

    return False

def getMatchingPatternOutput(pattern, patternRules):
    result = pattern
    # print "checking "+pattern
    for rule in patternRules:
        rulePattern = rule.split(" => ")[0]
        ruleOutput = rule.split(" => ")[1]
        if patternMatch(pattern, rulePattern):
            result = ruleOutput
            # print "pattern "+pattern+" matches on rule "+rulePattern+" ouput "+ruleOutput+"!"
    return result

def breakUpAndTransform(pattern, squareSize):

    patternSize = pattern.count("/")+1
    patternBits = pattern.split("/")
    numberOfSquares = patternSize / squareSize
    result = ""

    # print "breaking up pattern with square size " + str(squareSize)
    # print "number of squares "+str(numberOfSquares)
    for ySquare in range(numberOfSquares):
        newPatternsCombinedRow = ""
        for xSquare in range(numberOfSquares):
            subPattern = ""
            for y in range(squareSize):
                line = patternBits[(ySquare*squareSize)+y][(xSquare*squareSize) : (xSquare*squareSize)+squareSize]
                # print line
                if subPattern == "":
                    subPattern = line
                else:
                    subPattern += "/" + line

            ruleOutput = getMatchingPatternOutput(subPattern, patternRules)

            if newPatternsCombinedRow == "":
                newPatternsCombinedRow = ruleOutput
            else:
                outputLines = ruleOutput.split("/")
                newPatternsCombinedRowLines = newPatternsCombinedRow.split("/")
                for line_idx in range(len(outputLines)):
                    newPatternsCombinedRowLines[line_idx] += outputLines[line_idx]
                newPatternsCombinedRow = convertListToString(newPatternsCombinedRowLines)
        if result == "":
            result = newPatternsCombinedRow
        else:
            result += "/" + newPatternsCombinedRow

    return result

def iteratePattern(pattern, patternRules):
    patternSize = pattern.count("/")+1
    if patternSize == 2 or patternSize == 3:
        return getMatchingPatternOutput(pattern, patternRules)
    else:
        patternBits = pattern.split("/")
        if patternSize % 2 == 0:
            return breakUpAndTransform(pattern, 2)
        else:
            return breakUpAndTransform(pattern, 3)

#no match
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("###/###/### => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == ".#./..#/###"

#basic pattern transform
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append(".#./..#/### => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#vertical flip
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("###/..#/.#. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#horizontal flip
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append(".#./#../### => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#rotateRight - size 3
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("#../#.#/##. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#rotateRight - size 2
pattern = "#./#."
patternRules = []
patternRules.append("../../.. => ..../..../..../....")
patternRules.append("##/.. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#rotateRightTwice - vertical flip / horizontal flip
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("###/#../.#. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#rotateRightThreeTimes - rotateRight / vertical flip / horizontal flip
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append(".##/#.#/..# => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#rotateRight / vertical flip
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("##./#.#/#.. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#rotateRight / horizontal flip
pattern = ".#./..#/###"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("..#/#.#/.## => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#sizeTwo pattern
pattern = ".#/.."
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append("../#. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..#/..../..../#..#"

#sizeFour pattern
pattern = ".#.#/..../.#.#/...."
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append(".#/.. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..##..#/......../......../#..##..#/#..##..#/......../......../#..##..#"

#sizeSix pattern
pattern = ".#.#.#/....../.#.#.#/....../.#.#.#/......"
patternRules = []
patternRules.append(".../.../... => ..../..../..../....")
patternRules.append(".#/.. => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..##..##..#/............/............/#..##..##..#/#..##..##..#/............/............/#..##..##..#/#..##..##..#/............/............/#..##..##..#"

#sizeNine pattern
pattern = "..#..#..#/........./..#..#..#/..#..#..#/........./..#..#..#/..#..#..#/........./..#..#..#"
patternRules = []
patternRules.append("..#/.../..# => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..##..##..#/............/............/#..##..##..#/#..##..##..#/............/............/#..##..##..#/#..##..##..#/............/............/#..##..##..#"

#sizeFifteen pattern
pattern = "..#..#..#..#..#/.............../..#..#..#..#..#/..#..#..#..#..#/.............../..#..#..#..#..#/..#..#..#..#..#/.............../..#..#..#..#..#/..#..#..#..#..#/.............../..#..#..#..#..#/..#..#..#..#..#/.............../..#..#..#..#..#"
patternRules = []
patternRules.append("..#/.../..# => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
print pattern == "#..##..##..##..##..#/..................../..................../#..##..##..##..##..#/#..##..##..##..##..#/..................../..................../#..##..##..##..##..#/#..##..##..##..##..#/..................../..................../#..##..##..##..##..#/#..##..##..##..##..#/..................../..................../#..##..##..##..##..#/#..##..##..##..##..#/..................../..................../#..##..##..##..##..#"

#test pattern
pattern = ".#./..#/###"
patternRules = []
patternRules.append("../.# => ##./#../...")
patternRules.append(".#./..#/### => #..#/..../..../#..#")
pattern = iteratePattern(pattern, patternRules)
pattern = iteratePattern(pattern, patternRules)
print pattern == "##.##./#..#../....../##.##./#..#../......"

#solve problem
print "---"
pattern = ".#./..#/###"
patternRules = []
f = open("c://temp//adcode.txt", "r")
for line in f:
    patternRules.append(line.strip())

print pattern
for i in range(1, 6):
    print "iteration "+str(i)
    pattern = iteratePattern(pattern, patternRules)
    print pattern
    print pattern.count("#")
