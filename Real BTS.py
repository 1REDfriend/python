station1 = input()
station2 = input()

price = 0

BTS = {
    "N" : [1,24],
    "E" : [1,23],
    "S" : [1,12],
    "W" : [1,1]
}

btsprice = [17,25,28,32,35,40,43,47]

if station1 == "N6" or station2 == "N6" :
    print("Error")
else :
    station1list = [i for i in station1]
    station2list = [i for i in station2]
    station1code = station1list[0]
    station2code = station2list[0]
    station1num = int(''.join([station1list[i] for i in range(1,len(station1list))]))
    station2num = int(''.join([station2list[i] for i in range(1,len(station2list))]))

    for i,v in BTS.items() :
        if i == station1code :
            if station1code == station2code :
                maxnum = max(station1num,station2num)
                minnum = min(station1num,station2num)
                counter = 0

                for num in range(minnum , maxnum + 1) :
                    if station1code == "N" :
                        if num not in range(8,25) :
                            counter += 1
                    elif station1code == "E" :
                        if num not in range(14,24) :
                            counter += 1

                if counter != -1 :
                    if counter <= len(btsprice) :
                        if counter != 0 :
                            price = btsprice[counter - 1]
                        else :
                            price = btsprice[counter]
                    else :
                        price = btsprice[len(btsprice) - 1]

                
                
                    