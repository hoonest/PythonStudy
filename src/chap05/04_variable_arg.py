# 가변 인자(매개변수) 모호성이 발생 가능성이 있는것 주의

def print_args1(argc, *argv):
    for i in range(argc):
        print(argv[i])

print_args1(3, '홍길동', '이순신', '강감찬')

#주의 : 가변매개변수의 앞에 정의되는 일반 매개변수는 키워드 매개변수를 이용할 수 없음
#print_args1(argc=3, '홍길동', '이순신', '강감찬')


def print_args2(*argv, argc):
    for i in range(argc):
        print(argv[i])

print_args2('홍길동', '이순신', '강감찬', argc=3)
#주의
#print_args2('홍길동', '이순신', '강감찬', 3)


