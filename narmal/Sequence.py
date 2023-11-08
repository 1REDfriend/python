startlist = []
startlist2 = []
count = 1
for i in range(int(input())) :
    for x in range(count) :
        startlist += "*"
        startlist += " "
    startlist += "\n"
    startlist = ''.join(startlist)
    count += 1
print(startlist)