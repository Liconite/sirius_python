price = int(input())
hours = int(input())

if 23 <= hours <= 9:
    print("Магазин закрыт")
elif 10 <= hours <= 12:
    print(price / 2)
elif 20 <= hours <= 22:
    print(price / 4)