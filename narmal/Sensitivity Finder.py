sensitive = 100.00
minValue, maxValue = 0, float('inf')

while True:
    print(f'{sensitive:.2f}?')
    sensitivity_feel = input()

    if sensitivity_feel == 'F':
        maxValue = min(maxValue, sensitive)
    elif sensitivity_feel == 'S':
        minValue = max(minValue, sensitive)
    elif sensitivity_feel == 'D':
        break

    if maxValue == float('inf'):
        sensitive *= 2
    else:
        sensitive = (minValue + maxValue) / 2

print(f'Your sensitivity is {sensitive:.2f}.')