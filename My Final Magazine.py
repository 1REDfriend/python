
bullet = int(input())
EnemyHealth = float(input())
bulletDM = float(input())

if (bullet != 0 and bulletDM != 0 and EnemyHealth != 0) :
    if (EnemyHealth // bulletDM) <= bullet :
        bulletremains = int(bullet - (EnemyHealth // bulletDM))
        print(f'dead : {int(bulletremains)} bullet remain')
    else :
        EnemyHealthremains = EnemyHealth - (bullet * bulletDM)
        print(f'alive : {EnemyHealthremains} health')
elif (bullet == 0 ) :
    print(f'alive : {EnemyHealth} health')
elif (EnemyHealth == 0) :
    print(f'dead : {int(bullet)} bullet remain')
else :
    print(f'alive : {EnemyHealth} health')