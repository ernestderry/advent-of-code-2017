def isAnagram(w1, w2):
    return sorted(list(w1)) == sorted(list(w2))

f = open("c:\\temp\\adcode.txt","r")

total = 0

for line in f:
  phraseList = line.split()
  wordCount = len(phraseList)
  foundAnagram = False
  for wordOneIdx in range(wordCount-1):
      for wordTwoIdx in range(wordOneIdx+1, wordCount):
          if isAnagram(phraseList[wordOneIdx], phraseList[wordTwoIdx]):
              foundAnagram = True
  if foundAnagram == False:
      total += 1

print total
