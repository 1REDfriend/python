boxX = int(input())
boxY = int(input())
starfield = int(input())

startdict = {

}

for i in range(boxY) :
    found = False
    i+=1
    for x,n in startdict.items() :
        x+=1
        print(x,i)
        if x is i :
            found = True
            startdict[i] += "*"
    if not found :
        startdict[i] = list("*")

print(startdict)