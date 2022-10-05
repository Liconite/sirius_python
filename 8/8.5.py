def grants(name, f_score):
    print(name)
    print("Итоговый счёт: " + str(f_score))
    if f_score > 80:
        return "Награждён грамотой"
    if 50 <= f_score <= 80:
        return "Наградить похвальной грамотой"
    if f_score < 50:
        return "Выдать грамоту об участии"


while True:
    name = input()
    if name == "Стоп":
        break
    else:
        score = sum(list(map(int, input().split())))
        print(grants(name, score))
