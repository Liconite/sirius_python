def sum_path(k):
    m = (k * 1000 // 140) + 1
    return 4 + m * 0.25


print(sum_path(int(input())))
