# ที่บริษัทแห่งหนึ่งมีนโยบายอยู่ว่าจะต้องให้ Bonus แก่พนักงานทุกคนในที่ทำงานแห่งนี้ ให้เงินโดย เอาจำนวนปี คูณกับ จำนวนเงินเดือนที่ได้ เช่น นาย A ทำงานมา 3 ปี เงินเดือนอยู่ที่ 10000 บาท Bonus ที่นาย A จะได้รับคือ 30000 บาท แต่ก็มีกฎอยู่อีกว่า
# 1.พนักงานคนใดที่ทำงานมากกว่าหรือเท่ากับ 10 เดือน ก็ถือว่าทำงานมาครบ 1 ปี เลย
# 2.จะต้องไม่มีพนักงานคนใดได้ Bonus เกิน 20 เท่าของเงินเดือน แม้จะทำงานมาเกิน 20 ปีก็ตาม
# 3.จะไม่มีพนักงานคนใดได้ Bonus น้อยกว่า 5000 บาท หรือ มากกว่า 1000000 บาท
# จงเขียนโปรแกรมคิดคำนวณ Bonus ของพนักงานในบริษัทนี้

moneypaypermont = int(input())
yearwork = int(input())
month = int(input())

if (month >= 10) :
    bonus = moneypaypermont * (yearwork + month//10)
    if (bonus < 5000) :
        print("5000")
    elif (bonus <= 1000000 and bonus <=  moneypaypermont * 20) :
        print(bonus)
    elif bonus >= moneypaypermont * 20 :
        if bonus > 1000000 :
            print("1000000")
        else :
            print(moneypaypermont * 20)
    elif (bonus >= 1000000) :
        print("1000000")

else :
    bonus = moneypaypermont * yearwork
    if (bonus < 5000) :
        print("5000")
    elif (bonus <= 1000000 and bonus <= moneypaypermont * 20) :
        print(bonus)
    elif (bonus >= moneypaypermont * 20 ):
        if bonus > 1000000 :
            print("1000000")
        else :
            print(moneypaypermont * 20)
    elif (bonus >= 1000000) :
        print("1000000")