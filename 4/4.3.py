login = input()
illegal = "=?*^$№@_"
for i in range(len(login)):
  if login[i] in illegal:
    print(login[i])