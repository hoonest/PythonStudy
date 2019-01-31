class Base:
    def __init__(self):
        print(self)
        self.messge='Hello, World.'

    def print_message(self):
        print(self.messge)

class Derived(Base):
    pass                    # Derived 클래스가 스스로 구현한 메서드는 없지만, Base로 부터 물려받은 print_messages()는 갖고 있음

if __name__ == '__main__':
    base = Base()
    base.print_message()
    dv = Derived()
    dv.print_message()