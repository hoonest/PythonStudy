a = 'Hello, Python'
print(a)

b = "Hello, Python"
print(b)


c = '''   # 도움말 or 설명에 사용하는 주석문
영원에 살고 순간에 살아라. 영원히 살 것처럼 일하고
금방 죽을 것처럼 사람들을 대하라.
           - 리히텐베르크
'''
print(c)

d = """
영원에 살고 순간에 살아라. 영원히 살 것처럼 일하고
금방 죽을 것처럼 사람들을 대하라.
           - 리히텐베르크
"""
print(d)
print(type(d))


# 문자열 연산( + , * )
print("Py" + "thon")
print("Py" "thon")

hello = 'Hello, '
world = 'World!!!'
helloWorld = hello+world
print(helloWorld)



# 주의
age = 25
#print('방가 방가' + age)    # error(문자열 + 문자열 외 자료형 허용하지 않는다)

print('python ' * 3)        # 문자열 반복

s = 'Good Morning'
print(s[0:4])
print(s[5:12])

a = s[:4]     # s[0:4]
b = s[5:]     # s[5:12]
c = s[-3:]    # 뒤로부터 카운트 시작(-1...) 출력 : "ing"
d = s[::2]    # 두 칸씩 카운팅


print(a)
print(b)
print(c)
print(d)
print(s)
print(s[2])                 # 특정 인덱스 위치 문자 반환

print('M' in s)
print('a' in s)
print('Good' in s)
print('evening' in s)

print(len(s))

# 형변환
print(type(str(3.14)))      # 입력 자료형 float -> 출력 자료형 'str'
print(type(int("49")))      # 입력 자료형 'str' -> 출력 자료형 int
print(type(float("23")))    # 입력 자료형 'str' -> 출력 자료형 float
print(type(complex("1+2j")))  # 입력 자료형 'str' -> 출력 자료형 complex


# str 객체 제공 메서드
##  - ppt 참조.


# 텍스트 -> 수
##  - input() : 사용자로부터 입력을 받아 프로그램에게 전달
##            : 반환형 -> 문자열

print("첫 번째 수 입력 : ")
a = input()
print("두 번째 수 입력 : ")
b = input()

# result = a * b  # error
result = int(a) * int(b)  # int() 생성자 호출

print("{0} * {1} = {2}".format(a, b, result))


# 수 -> 텍스트
import math

print(type(math.pi))

text = "원주율은 " + str(math.pi) + "입니다."
print(text)


# 비트 다루기
