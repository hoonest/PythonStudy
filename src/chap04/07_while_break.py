
while True:
    print('반복을 계속 할까요? : ')
    answer = input()

    if answer == 'y':
        print('반복을 계속합니다.')
    elif answer == 'n':
        print('반복을 종료 합니다.')
        break
    else:
        print('y or n으로 답하세요~')
print('반복이 종료 되었습니다.')