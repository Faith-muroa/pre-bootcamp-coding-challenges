def check65(num1, num2):
    if num1 == 65 or num2 == 65:
        return True
    elif num1 + num2 == 65:
        return True
    else:
        return False 

print(check65(63, 2))
print(check65(43, 65))
print(check65(65, 3))
print(check65(43, 7))
