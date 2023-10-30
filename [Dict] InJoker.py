skillMarble = {
    "QQQ" : "COLD SNAP",
    "QQW" : "GHOST WALK",
    "QQE" : "ICE WALL",
    "WWW" : "E.M.P",
    "WWQ" : "TORNADO",
    "WWE" : "ALACRITY" ,
    "EEE" : "SUN STRIKE",
    "EEQ" : "FORGE SPIRIT",
    "EEW" : "CHAOS METEOR",
    "QWE" : "DEFEANING BLAST"
}

skillList = []

skillInput = input()

# ถ้าเกิดมี R เข้ามา จะต้องมี s ตาม

for i in skillInput :
    skillList.append(i)
    if i == 'R' :
        break
print(skillList)