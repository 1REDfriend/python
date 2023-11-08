ph = float(input())

if (ph == 7) :
    print("neutral")
elif (ph < 7 and ph >= 0) :
    print("acidic")
elif(ph > 7 and ph <= 14) :
    print("akaline")
else :
    print("error")
