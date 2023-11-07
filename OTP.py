from collections import Counter
while 1 :
    otpcode = input()

    prelist = []
    otpCounter = {}
    otpCounter2 = []
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
        found = False
        for i in otpcode :
            count = otpcode.count(i)
            otpCounter2.append(count)
        for i in otpCounter2 :
            if i == 2 :
                if otpCounter2.count(i) == 4 :
                    found = True
            elif i == 3 :
                found = True

        if found :
            print("Valid")
        else :
            print("Invalid")

    elif len(otpcode) == 8 :
        found = False
        for i in otpcode :
            count = otpcode.count(i)
            otpCounter2.append(count)
        
        for i in otpCounter2 :
            if i == 3 :
                if otpCounter2.count(i) == 2 :
                    found = True
            elif i == 2 :
                if otpCounter2.count(i) == 3 :
                    found = True
        if found :
            print("Valid")
        else :
            print("Invalid")