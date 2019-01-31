import sys

#print("숫자를 입력하세요 : ")
#a = int(input())

#if a == 0 :
#    print('0은 나눗셈에 이용할 수 없습니다. ')
#    sys.exit(0)
#else:
#print('3/', a, '=', 3 / a)


print('요일(월~일)dmf 입력하세요 : ')
dayOfWeek = input()
if dayOfWeek == '월':
    print('Monday')
elif dayOfWeek == '화':
    print('Tuesday')
elif dayOfWeek == '수':
    print('Wednesday')
elif dayOfWeek == '목':
    print('Thursday')
elif dayOfWeek == '금':
    print('Friday')
elif dayOfWeek == '토':
    print('Saturday')
elif dayOfWeek == '일':
    print('Sunday')
else :
    print('잘못된 입력입니다.')