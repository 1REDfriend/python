while True:
    # รับข้อมูลจากผู้ใช้
    user_input = input()
    
    # ถ้าผู้ใช้ป้อน "0" ให้ออกจากลูป
    if user_input == '0':
        break
    
    # แปลงข้อมูลที่รับเข้ามาให้อยู่ในรูปสตริง
    num_str = str(user_input)
    
    # ตรวจสอบความยาวของตัวเลข
    if len(num_str) == 4:
        # กรณีตัวเลขสี่หลัก
        if len(set(num_str)) < 4:
            print("Valid")
        else:
            print("Invalid")
    elif len(num_str) == 6:
        # กรณีตัวเลขหกหลัก
        is_valid = False
        for i in range(4, len(num_str)):
            if num_str[i] == num_str[i-4]:
                if num_str.count(num_str[i]) == 2 or num_str.count(num_str[i]) == 3:
                    is_valid = True
                    break
        if is_valid:
            print("Valid")
        else:
            print("Invalid")

    elif len(num_str) == 8:
        # กรณีตัวเลขแปดหลัก
        is_valid = False
        for i in range(6, len(num_str)):
            if num_str[i] == num_str[i-2] and num_str.count(num_str[i]) == 3:
                is_valid = True
                break
        if is_valid:
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
