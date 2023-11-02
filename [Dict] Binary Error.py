
my_list = []

while True:
    text = input()
    if text.lower() != "end":
        found = False
        for item in my_list:
            if item[0] == text:
                item[1] += 1
                found = True
                break
        if not found:
            my_list.append([text, 1])
    else:
        break

for i in my_list :
    num = int(i[0]) + i[1]
    binary = "{0:b}".format(num)
    print(f'{i[0]}-->{binary}')
