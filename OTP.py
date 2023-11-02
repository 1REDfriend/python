while True:
    otp = input()
    
    if otp == "0":
        break
    
    if len(otp) == 4:
        duplicate_count = 0  # ตัวแปรเพื่อเก็บจำนวนตัวที่ซ้ำกัน
        for i in range(len(otp)):
            for j in range(i+1, len(otp)):
                if otp[i] == otp[j]:
                    duplicate_count += 1

        if duplicate_count == 1:
            print(f"Valid")
        else :
            print("Invalid")
    elif len(otp) == 6 :
        duplicate_count = 0  # ตัวแปรเพื่อเก็บจำนวนตัวที่ซ้ำกัน
        for i in range(len(otp)):
            for j in range(i+1, len(otp)):
                if otp[i] == otp[j]:
                    duplicate_count += 1

        
        if duplicate_count >= 2:
            print(f"Valid")
        else :
            print("Invalid")
    
