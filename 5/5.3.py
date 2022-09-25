grades = list(map(int, input().split()))
k_5 = grades.count(5)
k_4 = grades.count(4)
k_3 = grades.count(3)
k_2 = grades.count(2)

percent = 100 / len(grades) * k_5

print(percent)
