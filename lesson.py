a = int(input())
if a == 1:
    print(0)
elif a % 2 != 0:
    print('НЕТ')
else:
    step = 0
    while a != 1:
        a = a / 2
        step+=1
    print(step)


