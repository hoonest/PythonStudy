# super() : 부모 클래스의 객체 역할을 하는 프록시(proxy)를 반환하는 내장 함수

class A:
    def __init__(self):
        print('A.__init__()')
        self.message = 'hello'

class B(A):
    def __init__(self):
        print('B.__init__()')
        super().__init__()
        print('self.message is ' + self.message)

if __name__ == '__main__':
    b = B()


# 참조 : 자식 클래스의 인스턴스를 생성할 때 부모클래스
class Base:
    def __init__(self):
        self.message = 'hello2'
        print('Base')

class Derived(Base):
    pass

d = Derived()
print(d.message)
print('===================')


class Base2:
    def __init__(self):
        self.message = 'hello2'
        print('Base')

class Derived2(Base2):
    def __init__(self):
        Base2.__init__(self)
        print('Derived')

d = Derived2()
print(d.message)