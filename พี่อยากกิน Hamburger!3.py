hmPrice = int(input())
totalHmValue = int(input())
freeHmValue = int(input())
buy = int(input())

# ต้องการบวกของแถมกับการซื้อให้ได้ของแถมแล้วซื้อน้อยที่สุดตามจำนวนที่กำหนด
sumTotalHM = 0
sumTotalFreeHM = 0
finalBuy = 0

valuemax = max(totalHmValue , freeHmValue)
if totalHmValue < buy :
    sumTotalFreeHM = ((buy // valuemax) - 1) * freeHmValue
    sumTotalHM =  ((buy // valuemax) - 1) * totalHmValue
    if (sumTotalFreeHM + sumTotalHM) >= buy :
        print(f'{sumTotalFreeHM + sumTotalHM} ชิ้น')
        print(f'{sumTotalHM * hmPrice} บาท')
    else :
        print(f'{sumTotalHM + (buy - (sumTotalFreeHM + sumTotalHM))} ชิ้น')
        print(f'{hmPrice * (sumTotalHM + (buy - (sumTotalFreeHM + sumTotalHM)))} บาท')
else :
    print(f'{buy} ชิ้น')
    print(f'{buy * hmPrice} บาท')