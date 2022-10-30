def file2():
    with open('new.txt', 'w+') as f2:
        f2.write('но у меня не получается')
    with open('new+.txt', 'w+') as final:
        with open('new.txt', 'r+') as f1:
            with open('new+.txt', 'r+') as f2:
                final.write(f1.read() + ' ')
                final.write(f2.read())
    with open('join.txt', 'r+') as final1:
        print(final1.read())
