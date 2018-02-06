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

      insList[currentIns] += 1
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
