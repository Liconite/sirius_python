prices = list(map(int, input().split(", ")))
s_prices = sorted(prices)
rs_prises = sorted(prices, reverse=True)

if prices == s_prices:
    print("Акция")
    print(sum(prices)/2)
elif prices == rs_prises:
    print("Акция")
    print(sum(prices) / 3)
else:
    print("К оплате:", sum(prices))