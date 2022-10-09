def summa(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(len(arr)-1) + summa(arr)


m = list(map(int, input().split()))
print(summa(m))
