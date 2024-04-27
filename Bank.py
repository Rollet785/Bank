def show_menu():
    print("1. На еду")
    print("2. В интернете")
    print("3. Меня скамили")
    print("4. На учёбу")
    print("5. На технику")
    print('6. Завершить программу')


def ask_category():
    b = int(input('Сколько категорий сегодня было задействовано '))
    return b


def food_kategory():
    food = int(input('Расходы на еду '))
    return food


def internet_category():
    internet = int(input('Расходы в интернете '))
    return internet


def scam_category():
    scam = int(input('Сколько у вас отобрали мошенники '))
    return scam


def study_category():
    study = int(input('Расходы на самообразование '))
    return study


def technika_category():
    technika = int(input('Расходы на технику '))
    return technika


def not_money(food, internet, scam, study, technika, check):
    if food + internet + scam + study + technika > check:
        print('Недостаточно средств')
        print(f'Потраено {food + internet + scam + study + technika}')
        return True
    return False


def main():
    check = int(input('Текущий счёт '))
    food = 0
    internet = 0
    scam = 0
    study = 0
    technika = 0
    while True:
        show_menu()
        b = ask_category()
        if b == 6:
            print('Программа завершена')
            return
        if b != 1 and b != 2 and b != 3 and b != 4 and b != 5 and b != 6:
            print('error')
            ask_category()
        for i in range(b):
            a = int(input('На что вы тратили деньги сегодня (введите цифры от 1 до 5) '))
            if a == 1:
                food = food_kategory()
                if not_money(food, internet, scam, study, technika, check):
                    return
            elif a == 2:
                internet = internet_category()
                if not_money(food, internet, scam, study, technika, check):
                    return
            elif a == 3:
                scam = scam_category()
                if not_money(food, internet, scam, study, technika, check):
                    return
            elif a == 4:
                study = study_category()
                if not_money(food, internet, scam, study, technika, check):
                    return
            elif a == 5:
                technika = technika_category()
                if not_money(food, internet, scam, study, technika, check):
                    return
            elif a == 6:
                print('Программа завершена')
                return
            else:
                print('Error')
        wasted = food + internet + scam + study + technika
        left = check - wasted
        print(f'Осталось на счёте {left}')
        print(f'Потрачено {wasted}')
        print('Напишите 52, чтобы завершить программу. Если хотите продолжить, то введите любое другое число')
        c = int(input())
        if c == 52:
            print('Программа завершена')
            return
main()
