shelv = []

while 1 :
    book = input()
    if book.lower() == 'end' :
        break
    else :
        Found = False
        for i in shelv :
            if i[0] == book :
                i[1] += 1
                Found = True
        if not Found :
            shelv.append([book , 1])
finalshelv = []
for i,v in enumerate(shelv) :
    finalshelv.append([v[0],i+1,v[1]])

finalshelv.sort(key=lambda x: x[0])
for i in finalshelv :
    print(f"{i[0]} {i[1]} {i[2]}")