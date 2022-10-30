def file():
    with open('test.txt', 'w+') as f:
        f.write('Я гений и стараюсь учить питон')
    with open('test.txt', 'r+') as f:
        print((f.read())[0:7])
