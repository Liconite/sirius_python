def calculate(el):
    sr = sum(el) / len(el)
    b = []
    for i in range(len(el)):
        if el[i] > sr:
            b.append(el[i])
    return sr, b


l = list(map(int, input().split()))

print(calculate(l))
