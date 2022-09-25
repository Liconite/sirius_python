grades = list(map(int, input().split(", ")))

k_5 = grades.count(5)
k_4 = grades.count(4)
k_3 = grades.count(3)
k_2 = grades.count(2)
form = (k_5 + k_4 + k_3)/4*100

print(*grades)
print(k_2, k_3, k_4, k_5)
print(form)