'''МОДУЛЬ 3'''
year = int(input("Укажите год рождения А.С Пушкина: "))
if year != 1799:
    print("Неверный год рождения")
else:
    day = int(input("Укажите день рождения А.С Пушкина: "))
    if day == 6:
        print("Верно")
    else:
        print("Неверный день рождения")