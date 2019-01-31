# 데코레이터 사용 용도(생성자)

class MyDecorator:
    def __init__(self, f):
        print('initializing MyDecorator...')
        self.func = f       #MyDecorator의 func데이터 속성이 print_hello를 받아둠

    def __call__(self):
        print('Begin : {0}'.format(self.func.__name__))
        self.func()         # __call__()메서드가 호출되면 생성자에서 저장해둔 함수(데이터 속성)을 호출
        print('End : {0}'.format(self.func.__name__))

if __name__ == '__main__':
    def print_hello():
        print('hello.')

    d = MyDecorator(print_hello)
    d()