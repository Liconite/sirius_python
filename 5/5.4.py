surname_l = []
jobs_l = []
full_l= []

surname = input()
jobs = input()
marks_l = list(map(int, input().split(", ")))

surname_l.append(surname)
jobs_l.append(jobs)

full_l.append(surname_l)
full_l.append(jobs_l)
full_l.append(marks_l)

print(full_l)
