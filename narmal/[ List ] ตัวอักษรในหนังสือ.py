namelist = []

while 1 :
    count = 0
    text = input()
    
    if (text.lower() == "end") :
        break
    else :
        for i in text :
            count += 1
        namelist += [(count , text)]

namelist = sorted(namelist, key=lambda x:x[0])

for i in namelist :
    print(i[1])