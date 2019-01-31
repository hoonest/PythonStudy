print('수를 입력 :')

a = int(input())

if a > 10 and a % 2 == 0:
    print('10보다 큰 짝수')
elif a > 10 and a % 2 !=0:
    print('10보다 큰 홀수')
elif a < 10 and a % 2 == 0:
    print('10보다 작은 짝수')
else:
    print('10보다 작은 홀수')