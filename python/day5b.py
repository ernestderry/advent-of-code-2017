def exitSteps(insList):
   currentIns = 0
   listLength = len(insList)
   totalSteps = 0
   while True:
      totalSteps += 1

      if insList[currentIns] <> 0:
         newIns = currentIns + insList[currentIns]
      else:
         newIns = currentIns

      if insList[currentIns] >= 3:
          offset = -1
      else:
          offset = 1

      insList[currentIns] += offset
      currentIns = newIns
      if currentIns > (listLength - 1):
          break

   return totalSteps

f = open("c:\\temp\\adcode.txt","r")

instructionList = []
for line in f:
    instructionList.append(int(line))

print instructionList
print "answer " + str(exitSteps(instructionList))

print exitSteps([1]) == 1
print exitSteps([0]) == 2
print exitSteps([1, -1]) == 3
print exitSteps([1, 1, -2]) == 6
