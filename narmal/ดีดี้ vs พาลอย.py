didyHealth = float(input())
didyTotalDM = 0
# เมื่อดีดี้โดนโจมตีจนถึงในจุดที่กำหนดดีดี้จะสามารถโจมตีใส่ผู้ที่โจมตีดีดี้ได้แบบ 100%
didyReUseDM = 0.03
didyMaxReUseTotalDM = float(input())
# บรรทัด 1 เลือดของดีดี้(float)
# บรรทัด 2 ค่าการปรับตัวที่ต้องครบ(float)
# บรรทัด 3 จำนวนการโจมตีของพาลอย(int)
# บรรทัด n+1 แดมเมจที่พาลอยโจมทีในแต่ละที (float)
praployTotalDM = int(input())
for i in range(praployTotalDM) :
    plaployDM = float(input())
    didyTotalDM += plaployDM * didyReUseDM
    didyHealth -= plaployDM

if (didyHealth <= 0 ) :
    print("ดีดี้โดนัท") 
elif (didyHealth > 0 and didyTotalDM >= didyMaxReUseTotalDM) :
    print("พาลอยซาชิมิ")
elif (didyHealth > 0 and didyTotalDM <= didyMaxReUseTotalDM) :
    print("ตายคู่")