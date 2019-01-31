# 변수 (정수/실수)
a = 123456789
print(a)


# 10->16
print(hex(123))

### 16 진수 -> 10진수
print(0x3039)

### 2진수 -> 10진수  변환
print(0b1000)
print(0b11111111)

### 10진수 -> 8진수 변환
print(oct(8))
print(oct(12))


print(0o10)
print(0o15)

# 변수(실수)
h = 3.14
print(h)
print(type(h))   # <class 'float'>

# 연산자
b = 3.3 + 4.2
print(b)

c = 10.0 - 30.8
print(c)

d = 10.1 * 30.4
print(d)

e = 22.5 / 7.6  # 결과값 : 실수
print(e)
print(type(e))

f = 22.7 // 7.5 # 몫 반환 연산자
print(f)

g = 22.6 % 7.3  # 나머지
print(g)

k = 43.2 - 43.1
print(k)


a = (1+2j) + (3+4j)  # (a+bj) + (c + dj) = (a+c) + (b+d)
print(a)             # 4+6j

a = (1+2j) - (3+4j)  # (a+bj) + (c + dj) = (a-c) + (b-d)
print(a)             # -2-2j

a = (1+2j) * (3+4j)  # (a+bj) * (c + dj) = (ac-bd) + (bc-ad)
print(a)             # -5+10j

a = (1+2j) / (3+4j)  # (a+bj) * (c + dj) = (a+bj)(c-dj)/(c+dj)(c-dj)
                     #                   = ((ac+bd)/(c^2 + d^2)) + ((bc-ad)/(c^2+d^2)
print(a)             # 0.44+0.08j


# math 모듈을 이용한 계산
import math

print(math.pi)
print(math.e)

print(math.pow(3,3))
print(3**3)

print(math.sqrt(81))

print(27**(1/3))

print(math.pow(27, (1/3)))

print(math.log(4,2))


print(type(123))
