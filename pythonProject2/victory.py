'''МОДУЛЬ 6'''

ans = "Y"
while  ans == "Y" or ans == "y":
    right_answer = 0

    # 1799 - год рождения А.С Пушкина
    if int(input("Укажите год рождения А.С Пушкина: ")) == 1799:
        right_answer += 1

    # 1809 - год рождения Н.В. Гоголя
    if int(input("Укажите год рождения Н.В. Гоголя: ")) == 1809:
        right_answer += 1

    # 1821 - год рождения Ф.М. Достоевского
    if int(input("Укажите год рождения Ф.М. Достоевского: ")) == 1821:
        right_answer += 1

    # 1828 - год рождения Л.Н. Толстого
    if int(input("Укажите год рождения Л.Н. Толстого: ")) == 1828:
        right_answer += 1

    # 1860 - год рождения А.П Чехова
    if int(input("Укажите год рождения А.П Чехова: ")) == 1860:
        right_answer += 1

    print()
    print("Количество правильных ответов:", right_answer)
    print("Количество ошибок:", 5 - right_answer)
    print("Процент правильных ответов:", right_answer * 100 / 5)
    print("Процент неправильных ответов:", 100 - right_answer * 100 / 5)
    print()

    ans = ""
    while not (ans == "N" or ans == "n" or ans == "Y" or ans == "y"):
        ans = input("Желаете повторить? (Y/N):")



