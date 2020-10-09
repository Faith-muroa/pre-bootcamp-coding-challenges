def check3(num1, num2):
    if num1 == 3 or num2 == 3 and num1 + num2 == 3:
        return True
   
    else:
        return False

print(check3(3, 3))
print(check3(2, 8))
print(check3(3, 9))
print(check3(1, 2))


