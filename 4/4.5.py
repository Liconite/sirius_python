all = 0
while True:
  price = int(input())
  if price == 0:
    print("Итого:", all)
    break
  else:
    new_price = price / 2
    all += new_price
    print("Цена со скидкой:", new_price)