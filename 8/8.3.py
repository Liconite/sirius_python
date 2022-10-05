def dopusk(k):
    if k > 50:
        return "True"
    else:
        return "False\nВы отчислены"


stud_k = int(input())
for i in range(stud_k):
    score = int(input())
    print(dopusk(score))
