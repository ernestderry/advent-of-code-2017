def difference(line):
  listOfInts = map(int, line.split())
  difference = max(listOfInts) - min(listOfInts)
  return difference

f = open("c:\\temp\\adcode.txt","r")

total = 0

for line in f:
  total += difference(line)

print total
