sum = 0
threeMultiple = False
fiveMultiple = False

for i in range(3, 1000):
    threeMultiple = i % 3 == 0
    fiveMultiple = i % 5 == 0
    if (threeMultiple or fiveMultiple):
        sum += 1

print(sum)
 
