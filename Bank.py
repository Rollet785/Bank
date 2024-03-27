check = int(input('Изначальный счёт '))
print("1. На еду")
print("2. В интернете")
print("3. Меня скамили")
print("4. На учёбу")
print("5. На технику")
food = 0
internet = 0
scam = 0
study = 0
technika = 0
while True:
    b = int(input('Сколько категорий сегодня было задействовано '))
    flag = True
    for i in range(b):
        a = int(input('На что вы тратили деньги сегодня (введите цифры от 1 до 5 в столбик) '))
        if a == 1:
            food = int(input('Расходы на еду '))
            if food + internet + scam + study + technika > check:
                print('Недостаточно средств')
                flag = False
                break
        elif a == 2:
            internet = int(input('Расходы в интернете '))
            if food + internet + scam + study + technika > check:
                print('Недостаточно средств')
                flag = False
                break
        elif a == 3:
            scam = int(input('Сколько у вас отобрали мошенники '))
            if food + internet + scam + study + technika > check:
                print('Недостаточно средств')
                flag = False
                break
        elif a == 4:
            study = int(input('Расходы на самообразование '))
            if food + internet + scam + study + technika > check:
                print('Недостаточно средств')
                flag = False
                break
        elif a == 5:
            technika = int(input('Расходы на технику '))
            if food + internet + scam + study + technika > check:
                print('Недостаточно средств')
                flag = False
                break
    if flag == False:
        break
    wast = food + internet + scam + study + technika
    left = check - food - internet - scam - study - technika
    print(f'Осталось на счёте {left}')
    print(f'Потрачено {wast}')
    break
