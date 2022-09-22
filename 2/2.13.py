pr = input().split()
for i in range(len(pr)):
  if "@" in pr[i]:
    print(pr[i])