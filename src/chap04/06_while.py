print('몇 번 반복할까요? :')

limit = int(input())

count = 0
while limit > 0:
    count = count +1
    print('{0}회 반복.'.format(count))
    print('limit=', limit)
    limit = limit -1

print('반복이 종료 되었습니다. ')