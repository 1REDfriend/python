books = []
shelv = []
couter = 1

while True:
    bookcode = input()
    if bookcode.lower() == "end":
        break
    else :
        books.append(bookcode)


for i,v in enumerate(books) :
    # จะหาว่ามีหนังสืออยู่ใน shelv หรือป่าว ถ้าไม่ให้เพิ่ม books, i , 1
    # แต่ถ้ามี ให้ บวก จำนวนเพิ่ม
    if i == 0 :
        shelv.append((v , i+1 , 1))
    else :
        try:
            if (v in shelv) :
                print(v)
        except ValueError :
            shelv.append((v , i , 1))

for i in shelv :
    print(i[0],i[1],i[2])