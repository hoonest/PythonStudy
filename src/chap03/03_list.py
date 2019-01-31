# 리스트 저장 형태
a = ['홍길동', '강감찬', '이순신']
print(a)
print(type(a))

# 데이터 접근
print(a[0] + "==" + a[1] )

# 슬라이싱 기능
x = [1,2,3,4,5,6,7,8,9,10]

print(x[0:5])  # [1, 2, 3, 4, 5]
print(x[5:])   # [6, 7, 8, 9, 10]
print(x[:3])   # [1, 2, 3]

a = [1,2,3,4]
b = [5,6,7]
c = a+b
print(c)

a = [1,2,3,4,5]
a[2] = 30
print(a)

print(len(a))

a.append(6)
print(a)

a.extend([10,20,40])
print(a)

a.insert(2, 3)
print(a)
a.pop(3)
a.remove(40)
a.sort(reverse=True)
print(a)
a.sort()
print(a)
a.reverse()
print(a)


a = (1,2,3)
print(a)
print(type(a))
a = 1, 2, 3, 4
print(a)

b = 1,
print(b)
c = a + b

print(c)

print(c[3] + c[0])
print(len(c))

# 튜플 패킹
a = 1, 2, 3
print(a)
# 튜플 언패킹
data = 'seoul', 37.541, 126.986
city, latitude, longitude = data
print('city' + " " + "latitude" + " " + 'longitude')




b = ('abc', 'def','ghi', 'def')
print(b.index('def'))
print(b.count('def'))



dic = {}
dic['파이썬'] = 'www.python.org'
dic['MS'] = 'www.microsoft.com'
dic['애플'] = 'www.apple.com'
print(dic['파이썬'])
print(type(dic))

print(dic)
print(dic.keys())

print(dic.values())

print(dic.items())








