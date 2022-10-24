import random


def price():
    print(
        "300 bucks за месяц посещения"
    )
    return "\n"


def trainer_info():
    print(
        "Ваш тренер:\n"
        "Билли Харрингтон\n"
        "Номер тренера: 88005553535"
    )
    return "\n"


def timetable():
    print(
        "Расписание:\n"
        "Понедельник - воскресенье: круглосуточно"
    )
    return "\n"


def music():
    i = random.randint(0, 14)
    m = ["Can't Hold Us feat. Ray Dalton — Macklemore & Ryan Lewis, Ray Dalton",
         "Genesis — Justice",
         "Stronger — Kanye West",
         "BURN IT DOWN — Linkin Park",
         "There For You Madison Mars Remix — Martin Garrix, Troye Sivan",
         "Bad Boy Ken feat. Siri — Badpojken",
         "Smack My Bitch Up — The Prodigy",
         "#thatPOWER — will.i.am, Justin Bieber",
         "The Pretender — Foo Fighters",
         "Habits (Stay High) Hippie Sabotage Remix — Tove Lo, Hippie Sabotage",
         "We Own It (Fast & Furious) — 2 Chainz, Wiz Khalifa",
         "Good Feeling — Flo Rida",
         "Too Original feat. Elliphant & Jovi Rockwell",
         "Firestarter — The Prodigy",
         "Rollin' (Air Raid Vehicle) — Limp Bizkit"]
    print("Вот ваш трек для тренировки:", m[i])
    return "\n"


def sportbar():
    print("Протеиновый батончик - 120р\n"
          "Проnеиновый коктель - 150р (0.4 л), 200р (0.6 л)\n"
          "Вода (0.5) - 65р (негазированная), 70р (газированная)\n"
          )
    return "\n"


def abilities():
    print("\nЧтобы узнать расписание, введите команду 'Расписание'\n"
          "Чтобы узнать информацию про вашего тренера, введите команду 'Тренер'\n"
          "Чтобы узнать стоимость тренировки, введите команду 'Цена'\n"
          "Мы можем посоветовать вам трек для тренировки при помощи команды 'Музыка'\n"
          "Также у нас имеется спортбар, команда 'Спортбар' подскажет ассортимент"
          )
    return '\n'


def main(request):
    if "возможности" in request.lower() or "может" in request.lower() or "умеет" in request.lower():
        abilities()
    if "расп" in request.lower():
        timetable()
    if "трен" in request.lower():
        trainer_info()
    if "цен" in request.lower():
        price()
    if "музык" in request.lower() or "трек" in request.lower():
        music()
    if "меню" in request.lower() or "спортбар" in request.lower():
        sportbar()

    return ""
