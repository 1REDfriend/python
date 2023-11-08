my_list = []

while True:
    text = input()
    if text.lower() != "end":
        try :
            text = int(text)
        except ValueError :
            break
        found = False
        for item in my_list:
            if item[0] == text:
                item[1] += 1
                found = True
        if not found:
            my_list.append([text, 1])
    else:
        break
stacklist = []

for i in my_list :
    num = int(i[0]) + i[1]
    ขยะ = ''
    
    if num == 0:
        ขยะ = '0'
    else:
        while num > 0:
            ขยะ = str(num % 2) + ขยะ
            num //= 2
    stacklist.append([i[0],"-->",ขยะ])

stacklist.sort(key=lambda x: int(x[0]))
for i in stacklist :
    print(f'{i[0]}{i[1]}{i[2]}')