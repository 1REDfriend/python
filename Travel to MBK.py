travellist = {
    50 : "Taxi",
    40 : "BTS",
    25 : "Motocycle",
    8 : "Song Thaeo"
}

money = input()
try :
    if money.isdigit() :
        money = int(money)
        traveloga = []

        for i,v in travellist.items() :
            if i <= money :
                money = money - i
                traveloga.append(v)
                # print(money)

        # print(traveloga)
        if not traveloga :
            print("stay home")
        else :
            for i in traveloga :
                if i == "Song Thaeo" or i == "BTS":
                    print(f'{i}\nwalking')
                    break
                else :
                    print(f'{i}\nno walking')
                    break
    else :
        print("stay home")
except ValueError :
    print("stay home")

