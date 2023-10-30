lastValue = 0
currrentValue = 100.00
sensitive = 100.00
counter = 0
print(f'{currrentValue:.2f}?')

while True :
    word = input()
    currrentValue = abs(sensitive - lastValue)
    if (word == "S") :
        sensitive = (currrentValue * 2) + lastValue
    elif (word == 'F') :
        sensitive = (currrentValue / 2) + lastValue
    elif (word == "D") :
        break
    lastValue = currrentValue
    print(F'{sensitive:.2f}?')