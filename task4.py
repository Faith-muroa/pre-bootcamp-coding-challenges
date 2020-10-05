def check3(num1, num2):
    if num1 == 3 or num2 == 3:
        return True
    elif num1 + num2 == 3:
        return True
    else:
        return False

print(check3(23, 3))
print(check3(2, 8))
print(check3(3, 9))
print(check3(10, 20))

#def check3(num1, num2):
    #if num1 == 3 or num2 == 3:
        #return True
        
        #A = num1 + num2
        #A = str(A)
        #for i in A:
            #if i == "3":
                #return True
            #else:
                #return False

#print(check3(5, 3))
#print(check3(1, 2))
