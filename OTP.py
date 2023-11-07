
while 1 :
    otp = input()
    if otp == "0" :
        break

    counter = [
        otp.count(str(code) for code in range(8))
    ]

    if len(otp) == 4  and counter.count(2) is 1:
        print("Valid")

    elif len(otp) == 6 and counter.count(2) is 2 or counter.count(3) is 1 :
        print("Valid")

    elif len(otp) == 8 and counter.count(2) is 4 or counter.count(3) is 2 :
        print("Valid")

    else :
        print("Invalid")

# OTP ที่มี 4 หลัก จะต้องมีเลขซ้ำกัน 1 ตัว, 2 หลักเท่านั้น (1120, 0850, 4543)
# OTP ที่มี 6 หลัก จะต้องมีเลขซ้ำกัน 2 ตัว, 4 หลัก หรือ 1 ตัว 3 หลัก อีกสามหลักจะเป็นอะไรก็ได้ (151567, 997882, 321324, 115167, 987666)
# OTP ที่มี 8 หลัก จะต้องมีเลขซ้ำกัน 3 ตัว, 6 หลัก หรือ 2 ตัว 6 หลัก อีกสองหลักจะเป็นอะไรก็ได้ (11223345, 68682400, 84886044)
# โปรแกรมของคุณจะต้องรับ OTP มาเรื่อยๆ จนกว่าจะได้รับเลข 0 เข้ามา คือให้หยุดการรับข้อมูล