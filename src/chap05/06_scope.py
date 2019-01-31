# 변수의 유효 범위(scope)

def scope_test1():
    a = 1
    print('a:{0}'.format(a))

a = 0
scope_test1()
print('a:{0}'.format(a))


def scope_test2():
    global c            # 외부의 전역변수를 지역변수의 생성을 막느다
    print("2c=", c)
    c=1
    print('3c=:{0}'.format(c))



c = 0
print('1c:{0}'.format(c))

scope_test2()
print('4c:{0}'.format(c))

