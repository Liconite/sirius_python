def file3():
    name_1 = input()
    name_2 = input()
    full_name1 = '/Jennysin/Desktop/Projects/' + name_1
    full_name2 = '/Jennysin/Desktop/Projects' + name_2
    stack = []
    with open(full_name1, 'r+') as f1:
        for line in f1:
            stack.append(line)
    print(stack)
    with open(full_name2, 'w+') as f2:
        for i in range(0, len(stack)):
            f2.writelines(str(i + 1) + ': ' + stack[i])
    with open(full_name2, 'r+') as f3:
        print(f3.read())