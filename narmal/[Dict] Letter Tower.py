tower = {}

text = input()

for i in text:
    Found = False
    for key in tower:
        if key == i:
            tower[key] += 1
            Found = True
            break
    if not Found:
        tower[i] = 1

tower = dict(sorted(tower.items(), key=lambda item: (-item[1] , item[0].lower())))
print("_________")
for i,v in tower.items() :
    print(f'|{i} <-> {v}|')
print("*********")