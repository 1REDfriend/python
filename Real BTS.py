station1 = input()
station2 = input()

BTS = {
    "16-44" : ['N8', 'N7', 'N6', 'N5', 'N4', 'N3', 'N2', 'N1', '0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9' , 'W1', '0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6' , 'S7' , 'S8'],
    "15" : ['E10', 'E11', 'E12', 'E13', 'E14' , 'S9', 'S10', 'S11', 'S12'],
    "Free" : ['N9', 'N10', 'N11', 'N12', 'N13', 'N14', 'N15', 'N16', 'N17', 'N18', 'N19', 'N20', 'N21', 'N22', 'N23', 'N24' , 'E15', 'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23']
}

if station1 == "N6" or station2 == "N6" :
    print("Error")
else :
    for i,v in BTS:
        for n in v :
            if n == station1 or 