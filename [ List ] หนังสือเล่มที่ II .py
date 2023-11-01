books = {}
couter = 1
while True:
    line = input()
    if line == "end":
        break
    else :
        if len(books) == 0 :
            books.append((line , 1 , 1))
        else :
            try :
                if books.index(line) == line :
                    couter += 1
                    
            except ValueError :
                books.append((line , len(books) , 1))