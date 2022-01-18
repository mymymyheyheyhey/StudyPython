height = int(input('''1 이상의 정수로
크리스마스 트리의 높이를 입력하세요 '''))

for i in range(height):

    for j in reversed(range(height)):
        if j > i:
            print(' ', end = '')
        else:
            print('*', end = '')

    for j in range(height):
        if i > j:
            print('*', end = '')
        else: print(' ', end = '')

    print()