# 중첩 함수
import math

def stddev(*args):
    def mean():
        return sum(args) /len(args)
    def variance(m):
        total = 0
        for arg in args:
            total += (arg-m)**2
        return total / (len(args)-1)

    v = variance(mean())
    return math.sqrt(v)

print(stddev(2.3, 1.7, 3.8, 4.9, 1.0, 0.8 ))


def mean(args):
    return sum(args) / len(args)

def variance(m, args):
    total = 0
    for arg in args:
        total += (arg-m)**2
    return total / (len(args)-1)

def stddev2(*args):
    v = variance(mean(args), args)
    return math.sqrt(v)

print(stddev2(2.3, 1.7, 3.8, 4.9, 1.0, 0.8 ))



# pass : 기능의 구현을 잠시 미루자
def empty_function():       # void method(){}와 같은 역할
    pass






