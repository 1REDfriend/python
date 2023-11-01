lastList = [100.00,0.00]
sensitive = 0
prenum = 0
counter = 0
print('%.2f' % lastList[0] + "?")
while 1 :
    word = input()
    if (lastList[0] < lastList[1]) :
        prenum = lastList[0]
    else :
        prenum = lastList[1]

    if (word != "D") :
        if (word == "F") :
            sensitive = ((lastList[0] - lastList[1]) / 2) + prenum
        elif (word == "S") :
            if counter > 0 :
                sensitive = ((lastList[0] - lastList[1]) / 2) + prenum
            else :
                sensitive = ((lastList[0] - lastList[1]) * 2) + prenum
        print('%.2f' % sensitive + "?")
    else :
        break
    # print(lastList)
    lastList.insert(0 , sensitive)
    lastList.pop()


print('Your sensitivity is ' + '%.2f' % sensitive + ".")