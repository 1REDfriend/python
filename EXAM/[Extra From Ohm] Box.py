boxX = int(input())
boxY = int(input())
starfield = int(input())

startdict = {

}

for i in range(boxY) :
    found = False
    for x,n in startdict.items() :
        if x is i :
            found = True
            startdict.update(x,(n,"*"))
    if not found :
        startdict.fromkeys(i,"*")

print(startdict)