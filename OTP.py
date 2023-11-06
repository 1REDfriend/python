from collections import Counter
while 1 :
    otpcode = input()

    prelist = []
    otpCounter = {}
    if otpcode == "0" :
        break

    for i in otpcode :
        prelist.append(i)
    if len(otpcode) == 4 :
        otpCounter = Counter(prelist)
        Found = False
        for i,v in otpCounter.items() :
            if v >= 2 :
                print("Valid")
                Found = True
        if not Found :
            print("Invalid")
    elif len(otpcode) == 6 :
        otpCounter = Counter(prelist)
        found = False
        counter = 0
        for i,v in otpCounter.items() :
            if v == 3 :
                found = True
            elif v == 2 :
                counter += 1
        if counter >= 2 or found :
            print("Valid")
        else :
            print("Invalid")
    elif len(otpcode) == 8 :
        otpCounter = Counter(prelist)
        found = False
        counter = 0
        counter2 = 0
        for i,v in otpCounter.items() :
            if v == 2 :
                counter2 += 1
            elif v == 3 :
                counter += 1
        if counter >= 2 or counter2 >= 3 :
            print("Valid")
        else :
            print("Invalid")