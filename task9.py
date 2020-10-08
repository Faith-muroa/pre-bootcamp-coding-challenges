multiples = []
b = 1
while b < 1000:
    if b % 3 == 0 or b % 5 == 0:
        multiples.append(b)
    b = b + 1
print(multiples)
sums = 0
for i in sum_of_multiples:
    sums = sums + i
print(sums)
