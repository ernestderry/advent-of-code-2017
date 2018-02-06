def scoreGroups(stream):
    print stream
    score = 0
    charIdx = 0
    level = 0
    garbageOn = False
    ignoreNext = False
    while charIdx < len(stream):
        char = stream[charIdx]
        if not ignoreNext:
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
            else:
                ignoreNext = False

        else:
            ignoreNext = False

        charIdx += 1

    return score


print scoreGroups("a") == 0
print scoreGroups("{}") == 1
print scoreGroups("{{}}") == 3
print scoreGroups("{{{}}}") == 6
print scoreGroups("{}{}") == 2
print scoreGroups("{{}{}}") == 5
print scoreGroups("{{{},{},{{}}}}") == 16
print scoreGroups("{<a>,<a>,<a>,<a>}") == 1
print scoreGroups("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
print scoreGroups("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
print scoreGroups("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3
print scoreGroups("<<<<<{}>{<<<<<>}") == 1
print scoreGroups("{}<{}!!!>{}>{}") == 2

f = open("c://temp/adventCode.txt", "r")
for line in f:
    print "group score " + str(scoreGroups(line))
