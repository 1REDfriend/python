try :
    budget = float(input())

    if budget < 8:
        print("stay home")
    else:
        if budget >= 50:
            print("Taxi")
            print("no walking")
        elif budget >= 40:
            print("BTS")
            print("walking")
        elif budget >= 25:
            print("Motorcycle")
            print("no walking")
        else:
            print("Song Thaeo")
            print("walking")
except :
    print("stay home")