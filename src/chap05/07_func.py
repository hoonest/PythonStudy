#함수를 변수에 담아 사용

def print_something(a):
    print(a)

print_something(20)

p = print_something
p(123)
p('abc')

# 순서열 /딕셔너리에도 변수로 담아 보기

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

flist = [plus, minus]             # [] 리스트 형태 두개의 함수를 리스트로
print(plus(1, 2))
print(flist[0](1, 2))





