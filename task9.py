multiples = []
b = 1
while b < 1000:
    if b % 3 == 0 or b % 5 == 0:
        multiples.append(b)
        print(b)

    b = b + 1
print(multiples)

sum = 0
for i in multiples:
    sum = sum + i
print(sum)
