travellist = {
    50 : "Taxi",
    40 : "BTS",
    25 : "Motocycle",
    8 : "Song Thaeo"
}

money = int(input())
traveloga = []

for i,v in travellist.items() :
    if i <= money :
        money = money - i
        traveloga.append(v)
        print(money)

print(traveloga)
if not traveloga :
    print("No money to travel")
else :
    for i in traveloga :
        if i == "Song Thaeo" :
            print(f'{i}\nWalking')
        elif i == "BTS" :
            print(f'{i}\nNo Walk way')
