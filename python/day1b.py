a = <puzzle string>
length = len(a)
halfstep = length/2
b = a + a
total = 0

for idx in range(length):
    if a[idx] == b[idx+halfstep]:
        print a[idx]
        total += int(a[idx])

print "total " + str(total)
