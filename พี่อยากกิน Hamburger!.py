hmPrice = int(input())
totalHmValue = int(input())
freeHmValue = int(input())
buy = int(input())

# ต้องการบวกของแถมกับการซื้อให้ได้ของแถมแล้วซื้อน้อยที่สุดตามจำนวนที่กำหนด

if (totalHmValue <= buy) :
    
    sumTotalHmValue = totalHmValue
    sumTotalfreeHM = freeHmValue 

    while 1 :
        if (sumTotalHmValue != 0) :
            
            if (((sumTotalHmValue + sumTotalHmValue) < buy) and (buy // totalHmValue > 1)) : # อาจจะผิดตรง (buy // sumTotalHmValue > 1)
                sumTotalHmValue += totalHmValue
                sumTotalfreeHM += freeHmValue
                if (((sumTotalHmValue + sumTotalHmValue) >= buy)) :
                    sumTotalHmValue -= totalHmValue
                    sumTotalfreeHM -= freeHmValue
                    print(sumTotalHmValue)
            else :
                print(sumTotalHmValue ,sumTotalfreeHM)

                finalBuy = 0
                if (sumTotalHmValue + sumTotalfreeHM <= buy) :
                    finalBuy = (buy - (sumTotalHmValue + sumTotalfreeHM)) + sumTotalHmValue
                    finalTotalHM = buy
                else :
                    finalBuy = sumTotalHmValue
                    finalTotalHM = sumTotalHmValue + sumTotalfreeHM
                print(f'{finalTotalHM} ชิ้น')
                print(f'{finalBuy * hmPrice} บาท')
                break
        else :
            if (sumTotalfreeHM < buy) :
                sumTotalfreeHM += freeHmValue
            else :
                print(f'{sumTotalfreeHM} ชิ้น')
                print("0 บาท")
                break
else : 
    print(f'{buy} ชิ้น')
    print(f'{buy * hmPrice} บาท')

# ขาย Hamburger ราคา a บาท 
# เมื่อซื้อครบ b ชิ้น จะได้ฟรี c ชิ้น 
# ซึ่งพี่อยากกินทั้งหมด d ชิ้น 
# 
# พี่ต้องจ่ายเงินน้อยที่สุดกี่บาทถึงจะได้กินเบอร์เกอร์เพียงพอกับที่พี่อยากกิน(เกินได้แต่ห้ามขาด)