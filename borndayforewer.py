# День рождения Пушкина 06.06.1799
def pushkin():
    day = input('В какой день июня родился Пушкин?')
    if day == '06' or day == '6':
        print("Верно")
    else:
        print("Не верно")
    month = input('В какой месяц июня родился Пушкин?')
    if month == '06' or month == '6':
        print("Верно")
    else:
        print("Не верно")
    year = input('Введите год рождения А.С.Пушкина:')
    if year == '1799':
        print("Верно")
    else:
        print("Не верно")
    return


pushkin()
