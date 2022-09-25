games = []

while True:
  game_title = input("Введите название игры: ")
  if game_title == "0":
    games.sort()
    print(games)
    break
  else:
    if game_title in games:
      print("Эта игра уже записана")
    else:
      games.append(game_title)