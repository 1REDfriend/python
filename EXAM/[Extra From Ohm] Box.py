boxX = int(input())
boxY = int(input())
starfield = int(input())

startdict = {

}

# make colum

for i in range(boxY) :
    found = False
    i+=1
    startdict[i] = list("*")

# push star in dict

current_stardictY = boxY 
def next_stardictY () :
    if current_stardictY < 0 :
        current_stardictY = boxY
    else :
        current_stardictY -= 1
    return current_stardictY

for i in range(starfield) :
    startdict[next_stardictY()].append("*")
print(startdict)