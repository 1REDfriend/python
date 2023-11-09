name1 = input()
name2 = input()
name3 = input()
price = 0
def checkPrice(name) :
    if name == "Kai Thot" :
        return 25
    elif name == "Khao Mu Krop" :
        return 50
    elif name == "Mu Krathiam" :
        return 45
    elif name == "Pla Nin Thot" :
        return 80
    elif name == "Khaoniao" :
        return 5
price = checkPrice(name1) + checkPrice(name2) + checkPrice(name3)
print(f'{price} Baht')