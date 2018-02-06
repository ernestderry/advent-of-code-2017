a = <puzzle string>
b = a + a[0]
total = 0


for idx in range(len(a)):
    if a[idx] == b[idx+1]:
        print a[idx]
        total += int(a[idx])
print "total " + str(total)
