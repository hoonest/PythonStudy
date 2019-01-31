# 호출자에게 반환하기


def multiply(a,b):
    return  a*b           # return -> 1. 함수를 즉시 종료, 2. 호출자에게 결과 전달


result = multiply(3, 4)
print( 'multiply(3, 4) result = ',  result)


# 한 함수 안에 여러개의 return 배치 가능
def my_abs1(arg):
    if(arg<0):
        return arg * -1
    else:
        return arg


print(my_abs1(-1), "====", my_abs1(4))

print(my_abs1(0))


def my_abs2(arg):
    if(arg<0):
        return arg * -1
    elif(arg>0):
        return arg

print(my_abs2(0))



def ogamdo(num):
    for i in range(1, num+1):
        print('제 {0}의 아해'.format(i))
        if i == 5:
            return                # 반환데이터 없이 함수 종료의 의미로 사용
ogamdo(3)
ogamdo(5)
ogamdo(8)



def print_something(*args): #3. 반환결과 없고, 함수 중간에 종료시킬 일도 없을때 return 문 생략가능
    for s in args:
        print(s)

print_something(1, 2, 3, 4, 5)

