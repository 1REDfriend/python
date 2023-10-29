minimum = 50.00
maximum = 100.00

counter = 0
lastword = ''
print('%.2f' % maximum + "?")
while 1 :
    word = input()
    counter += 1

    if (word != "D") :
        if (word == "F") :
            maximum -= minimum
            lastword = 'F'
            minimum /= 2
        elif (word == "S") :
            minimum *= 2
            maximum += minimum
            lastword = 'S'
        print('%.2f' % maximum + "?")
    else :
        break
    if (lastword == word) :
        minimum /= 2

print('Your sensitivity is ' + '%.2f' % maximum + ".")