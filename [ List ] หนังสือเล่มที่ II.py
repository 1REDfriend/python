books = []
shelv = []
couter = 1

while True:
    bookcode = input()
    if bookcode == "end":
        break
    else :
        books.append(bookcode)


for i,v in enumerate(books) :
    # จะหาว่ามีหนังสืออยู่ใน shelv หรือป่าว ถ้าไม่ให้เพิ่ม books, i , 1
    # แต่ถ้ามี ให้ บวก จำนวนเพิ่ม

for i in shelv :
    print(i[0],i[1],i[2])