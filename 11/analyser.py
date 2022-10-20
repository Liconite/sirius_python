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
        "Расписание\n"
        "Понедельник - воскресенье: круглосуточно"
    )
    return "\n"


def main(request):
    if "расп" in request.lower():
        timetable()
    elif "трен" in request.lower():
        trainer_info()
    elif "цен" in request.lower():
        price()
    return None
