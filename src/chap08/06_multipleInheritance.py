# 다중 상속 주의 : 죽음의 다이어몬드

class A:
    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('C')

class D(C, B):
    pass


if __name__ == '__main__':
    d = D()
    d.method()            # B-D는