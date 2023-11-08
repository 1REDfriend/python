study1 = int(input())
study2 = int(input())
study3 = int(input())
study4 = int(input())
study5 = int(input())
percenStudy = float(input())
day = int(input())
notPass = 0

# อิจิกะ ทุก 1 วันที่สอน จะสามารถเรียนรู้ได้ a % ของสิ่งที่เรียนไปในวันนั้น.
# นิโนะ ทุก 1 วันที่สอน จะสามารถเรียนรู้ได้ b % ของสิ่งที่เรียนไปในวันนั้น.
# มิคุ ทุก 1 วันที่สอน จะสามารถเรียนรู้ได้ c % ของสิ่งที่เรียนไปในวันนั้น.
# ยตสึบะ ทุก 1 วันที่สอน จะสามารถเรียนรู้ได้ d % ของสิ่งที่เรียนไปในวันนั้น.
# อิตสึกิ ทุก 1 วันที่สอน จะสามารถเรียนรู้ได้ e % ของสิ่งที่เรียนไปในวันนั้น.

# โดยฟูทาโระจะทำการสอนพวกนี้ f % ต่อวัน
# เพราะในอีก g วัน ก็จะถึงการสอบปลายภาคแล้ว!!!
# สอบผ่านกันไม่เกินครึ่ง(ก็คือถ้ามีคนผ่านไม่เกิน 3 คน นั่นแหละ) จะทำให้ฟูทาโระตกงาน!!

# สอบผ่านคือเรียนรู้ได้เกิน 60 %
# หมายความว่าถ้าในระยะเวลาวันที่สอนแล้วเรียนรวมกันได้เกิน 60 % ก็จะสอบผ่าน


# ต้องเอาเปอร์เซนการสอนมาคูณหาเปอร์เซนของสิ่งที่น้องๆสามารถรับได้ แล้วนำไปคูณกับจำนวนวัน ก็จะได้เปอร์เซนที่น้องๆเรียนรู้ได้ในวันก่อนสอบ
canStudy1 = (percenStudy * study1/100) * day
canStudy2 = (percenStudy * study2/100) * day
canStudy3 = (percenStudy * study3/100) * day
canStudy4 = (percenStudy * study4/100) * day
canStudy5 = (percenStudy * study5/100) * day

if (canStudy1 <= 60) :
    print("Ichika : Fail")
    notPass += 1
else:
    print("Ichika : Pass")

if (canStudy2 <= 60) :
    print("Nino : Fail")
    notPass += 1
else:
    print("Nino : Pass")

if (canStudy3 <= 60) :
    print("Miku : Fail")
    notPass += 1
else:
    print("Miku : Pass")

if (canStudy4 <= 60) :
    print("Yotsuba : Fail")
    notPass += 1
else:
    print("Yotsuba : Pass")

if (canStudy5 <= 60) :
    print("Itsuki : Fail")
    notPass += 1
else:
    print("Itsuki : Pass")

if (notPass >= 3 ) :
    print("Futaro Outtt!!!")