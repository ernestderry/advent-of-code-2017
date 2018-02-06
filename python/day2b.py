def sumOfTwoNumbersThatEvenlyDivide(line):
  listOfInts = map(int, line.split())
  lineSize = len(listOfInts)
  for idx1 in range(lineSize):
      for idx2 in range(idx1+1,lineSize):
          num1 = listOfInts[idx1]
          num2 = listOfInts[idx2]
          if num1 > num2:
            if num1 % num2 == 0:
              result = num1/num2
              return result
          elif num2 % num1 == 0:
              result = num2/num1
              return result
  return 0

f = open("c:\\temp\\adcode.txt","r")

total = 0

for line in f:
  total += sumOfTwoNumbersThatEvenlyDivide(line)

print total
