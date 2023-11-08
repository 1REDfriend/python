
bullet = int(input())
EnemyHealth = float(input())
bulletDM = float(input())

for i in range(bullet) :
    if EnemyHealth > 0 and bullet > 0:
        EnemyHealth -= bulletDM
        bullet -= 1
    else :
        break

if ()