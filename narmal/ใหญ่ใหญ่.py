import re
# รับข้อความเข้ามา
input_text = input()

# แยกคำออกจากข้อความ
words = input_text.split()

# แปลงตัวอักษรแรกของแต่ละคำเป็นตัวใหญ่และรักษาสัญลักษณ์ "-" และ "_"
capitalized_words = []
for word in words:
    if word:
        parts = re.split('([-_])', word)  # แยกตัวอักษร "-" และ "_" ด้วยการใช้พิเศษใน re
        new_parts = [part.capitalize() if len(part) > 1 else part for part in parts]
        capitalized_word = ''.join(new_parts)
        capitalized_words.append(capitalized_word)

# รวมคำเป็นข้อความใหม่
capitalized_text = ' '.join(capitalized_words)

# พิมพ์ข้อความที่ผ่านการแปลง
print(capitalized_text)
