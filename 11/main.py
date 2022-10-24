import analyser as an


if __name__ == '__main__':
    print("Добро пожаловать в спортзал «Dungeon Master»")
    while True:
        print("\nВведите команду 'Возможности', чтобы узнать, что умееет бот")
        req = input("Что вас интересует? ")
        if req.lower() != "ничего":
            an.main(req)
        else:
            print("Ждём вам!")
            break

