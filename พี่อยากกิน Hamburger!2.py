hmPrice = int(input())
totalHmValue = int(input())
freeHmValue = int(input())
buy = int(input())

# ต้องการบวกของแถมกับการซื้อให้ได้ของแถมแล้วซื้อน้อยที่สุดตามจำนวนที่กำหนด
sumTotalHM = 0
sumTotalFreeHM = 0
finalBuy = 0

if (totalHmValue + freeHmValue < buy) :
    if (totalHmValue != 0) : # หาว่า แฺฮม ที่มีโปร อยู่ไม่เท่ากับ 0 นะ เดี่ยวเข้า เช็ค บัค
        if (buy//(totalHmValue + freeHmValue) <= 1) :
            if (totalHmValue < freeHmValue) :
                sumTotalHM = totalHmValue + totalHmValue
                sumTotalFreeHM = freeHmValue + freeHmValue
                print(f'{sumTotalHM + sumTotalFreeHM} ชิ้น')
                print(f'{sumTotalHM * hmPrice} บาท')
            else :
                finalBuy = totalHmValue + (buy - (totalHmValue + freeHmValue))
                print(f'{buy} ชิ้น')
                print(f'{finalBuy * hmPrice} บาท')
        else :
            finalBuy = buy//(totalHmValue + freeHmValue)
            sumTotalHM = finalBuy * totalHmValue
            sumTotalFreeHM = finalBuy * finalBuy
            if ((sumTotalHM + sumTotalFreeHM) < buy) :
                finalBuy = sumTotalHM + (buy - (sumTotalHM + sumTotalFreeHM)) # จะได้จน.ชิ้นที่ต้องชื้อมา
                print(f'{finalBuy + sumTotalFreeHM} ชิ้น')
                print(f'{finalBuy * hmPrice} บาท')
            else :
                finalBuy = sumTotalHM
                print(f'{finalBuy} ชิ้น')
                print(f'{finalBuy * hmPrice} บาท')
    else :
        if (((buy//freeHmValue)*freeHmValue) < buy) :
            finalBuy = ((buy//freeHmValue)*freeHmValue) + freeHmValue
            print(f'{finalBuy} ชิ้น')
            print(f'0 บาท')
        else :
            finalBuy = ((buy//freeHmValue)*freeHmValue)
            print(f'{finalBuy} ชิ้น')
            print(f'0 บาท')
else :
    if (totalHmValue > buy) :
        finalBuy = buy
        print(f'{finalBuy} ชิ้น')
        print(f'{finalBuy * hmPrice} บาท')
    else :
        finalBuy = totalHmValue
        print(f'{finalBuy + freeHmValue} ชิ้น')
        print(f'{finalBuy * hmPrice} บาท')
# ขาย Hamburger ราคา a บาท 
# เมื่อซื้อครบ b ชิ้น จะได้ฟรี c ชิ้น 
# ซึ่งพี่อยากกินทั้งหมด d ชิ้น 
# 
# พี่ต้องจ่ายเงินน้อยที่สุดกี่บาทถึงจะได้กินเบอร์เกอร์เพียงพอกับที่พี่อยากกิน(เกินได้แต่ห้ามขาด)