def discount(k):
    if 0 <= k <= 49:
        return "Скидка 10%"
    if 50 <= k <= 99:
        return "Скидка 15%"
    if k >= 100:
        return "Скидка 20%"

print(discount(int(input())))
