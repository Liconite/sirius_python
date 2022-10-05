def personal_badge(name, group):
    print("Колледж Сириус»")
    print("Имя: " + name)
    print("Группа: " + group)
    return "\n"


k = int(input())
for i in range(k):
    name, group = input(), input()
    print(personal_badge(name, group))
else:
    print("Готово! Заберите бейджики.")