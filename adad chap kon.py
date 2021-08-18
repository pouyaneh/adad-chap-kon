num = input()
for i in num:
    print(i + ':', end=' ')
    for _ in range(int(i)):
        print(i , end='')
    print()
