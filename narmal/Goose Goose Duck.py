import json
json.loads('[1, 2, 3, 3.1415, 6.8, "String", [1, "Nested"]]')

Goosedict = {}
duckdielist = []

while 1 :
    dictduck = input()
    if dictduck.lower() == "start" :
        break
    else :
        Goosedict.update(json.loads(dictduck))
while 1 :
    duckname = input()
    if duckname.lower() == "end" :
        break
    else :
        duckdielist.append(duckname)

ducktotal = 0
for i,v in Goosedict.items() :
    if v.lower() == "duck" :
        ducktotal += 1

for v in duckdielist :
    for i,u in Goosedict.items() :
        if v == i and u.lower() == "duck" :
            ducktotal -= 1

print(f'{ducktotal} Ducks Remains')
print("***Alive***")
duckdie = {}
for i,v in Goosedict.items() :
    if i in duckdielist :
        duckdie[i] = v
for i in duckdie.keys() :
    Goosedict.pop(i)

myKeys = list(Goosedict.keys())
myKeys.sort()
Goosedict = {i: Goosedict[i] for i in myKeys}

for i,v in Goosedict.items() :
    print(f'{i} : {v}')
print("***Dead***")

myKeys = list(duckdie.keys())
myKeys.sort()
duckdie = {i: duckdie[i] for i in myKeys}

for i,v in duckdie.items() :
    print(f'{i} : {v}')