# 데코레이터

class Callable:
    def __init__(self):
        print('init')

    def __call__(self):
        print('I am called.')
        self.message = 'hello'

    def method(self):
        print('method')

if __name__ == '__main__':
    obj = Callable()

    obj()