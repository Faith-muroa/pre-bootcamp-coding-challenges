def tempF(tempC):
    # tempF = Temperature in fahrenheit
    # tempC = Temperature in celcius
    return tempC * 9/5 + 32

print(tempF(65))

def tempC(tempF):
    return (tempF - 32) * 5/9 

print(tempC(54))
