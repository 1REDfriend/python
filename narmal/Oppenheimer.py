import math
boom = int(input())
stay = int(input())
radius = math.pi * boom**2
safeArea = radius*2

if ( stay < safeArea + 1) :
    print("Not Safe")
else :
    print("Safe")