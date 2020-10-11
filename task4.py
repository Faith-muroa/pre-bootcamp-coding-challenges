def func(num1, num2):
    if (num1 == 3 or num2 == 3) and "3" in str(num1 + num2):
        return True
   
    else:
        return False

print(func(3, 30))
print(func(2, 8))
print(func(3, 10))
print(func(1, 2))


