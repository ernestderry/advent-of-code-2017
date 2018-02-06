f = open("c:\\temp\\adcode.txt","r")

total = 0

for line in f:
  phraseList = line.split()
  phraseSet = set(phraseList)
  if len(phraseList) == len(phraseSet):
      print line
      total += 1

print total
