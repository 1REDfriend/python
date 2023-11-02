namelist = []

while 1 :
    count = 0
    text = input()
    for i in text :
        count += 1
    namelist += [(count , text)]
    if (text == "END") :
        break

namelist = sorted(namelist, key=lambda x:x[0])

print(namelist)