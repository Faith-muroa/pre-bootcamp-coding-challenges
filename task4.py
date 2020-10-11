def check3(num1, num2):
    if (num1 == 3 or num2 == 3) and "3" in str(num1 + num2):
        return True
    
    else:
        return False

print(check3(3, 30))
print(check3(2, 8))
print(check3(3, 10))
print(check3(10, 20))


