time = int(input("input : "))

day = int((time/60)/60)//24
hour = int(((time/60)//60) - (day * 24))
minute = int((time//60) - ((hour * 60) + (day * 24 * 60)))
second = int(time - (((minute * 60) + (hour * 60 * 60) + (day * 24 * 60 * 60))))

print(f'raw day = {day * 24} | raw hour = {(time/60)//60}')