# made in vs code ????
# รับจำนวนหนังสือ
n = int(input())

# สร้างรายชื่อหนังสือและชั้นวางหนังสือ
bookshelf = []
shelves = []

# อ่านชื่อหนังสือและจัดเก็บลงในรายชื่อหนังสือ
for i in range(n):
    book = input()
    bookshelf.append(book)

# วนลูปเพื่อจัดหนังสือ
for book in bookshelf:
    # หาชั้นวางหนังสือที่มีหนังสือชื่อเดียวกัน (ถ้ามี)
    found = False
    for shelf in shelves:
        if book in shelf:
            # ตรวจสอบว่ามีหนังสือชื่อเดียวกันในชั้นมากกว่า 2 เล่มหรือไม่
            if shelf.count(book) < 2:
                shelf.append(book)
            found = True
            break

    # ถ้าไม่เจอชั้นวางหนังสือที่มีหนังสือชื่อเดียวกัน
    if not found:
        # สร้างชั้นวางหนังสือใหม่และใส่หนังสือนี้ลงไป
        new_shelf = [book]
        shelves.append(new_shelf)
        
# แสดงผลลัพธ์
sunwang = []
for i, shelf in enumerate(shelves, start=1):
    for o in shelf :
        sunwang.append(o)
print(f'ชั้นวางหนังสือ {sunwang}')