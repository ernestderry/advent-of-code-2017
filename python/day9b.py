def scoreGroups(stream):
    print stream
    score = 0
    charIdx = 0
    level = 0
    garbageOn = False
    ignoreNext = False
    garbageCharsCount = 0
    while charIdx < len(stream):
        char = stream[charIdx]
        if not ignoreNext:
            garbageChar = False
            if not garbageOn:
                if char == "{":
                    level += 1
                    score += level
                if char == "}":
                    level -= 1
                if char == "<":
                    garbageOn = True
            elif char == ">":
                garbageOn = False
            else:
                garbageChar = True

            if char == "!":
                ignoreNext = True
                garbageChar = False
            else:
                ignoreNext = False

            if garbageChar:
                garbageCharsCount += 1

        else:
            ignoreNext = False

        charIdx += 1

    return [score, garbageCharsCount]



print scoreGroups("a")[0] == 0
print scoreGroups("{}")[0] == 1
print scoreGroups("{{}}")[0] == 3
print scoreGroups("{{{}}}")[0] == 6
print scoreGroups("{}{}")[0] == 2
print scoreGroups("{{}{}}")[0] == 5
print scoreGroups("{{{},{},{{}}}}")[0] == 16
print scoreGroups("{<a>,<a>,<a>,<a>}")[0] == 1
print scoreGroups("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
print scoreGroups("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
print scoreGroups("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3
print scoreGroups("<<<<<{}>{<<<<<>}")[0] == 1
print scoreGroups("{}<{}!!!>{}>{}")[0] == 2

f = open("c://temp/adventCode.txt", "r")
for line in f:
    print "group score " + str(scoreGroups(line)[0])
    print "garbage count " + str(scoreGroups(line)[1])
