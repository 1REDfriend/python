def is_valid_otp(otp):
    otp_str = str(otp)
    
    if len(otp_str) % 2 == 0:
        # OTP มีจำนวนหลักคู่ (4, 6, 8)
        digit_count = {}
        
        for digit in otp_str:
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
        
        # ตรวจสอบเงื่อนไขตามความยาวของ OTP
        if len(otp_str) == 4 and 1 in digit_count.values() and 2 in digit_count.values():
            return "Valid"
        elif len(otp_str) == 6 and (2 in digit_count.values() or 1 in digit_count.values()) and 4 in digit_count.values():
            return "Valid"
        elif len(otp_str) == 8 and (3 in digit_count.values() or 2 in digit_count.values()) and 6 in digit_count.values():
            return "Valid"
        else:
            return "Invalid"
    else:
        # OTP มีจำนวนหลักคี่ ไม่ถูกต้อง
        return "Invalid"

# รับ OTP จากผู้ใช้เรื่อยๆ จนกว่าจะรับค่า 0
while True:
    otp = int(input())
    if otp == 0:
        break
    result = is_valid_otp(otp)
    print(result)
