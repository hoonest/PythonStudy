from abc import  ABCMeta                # abc 모듈의 ABCMeta
from abc import abstractmethod          # abc 모듈의 abstractmethod 데코레이터

class AbstractDuck(metaclass=ABCMeta):  # metaclass : 클래스에 대한 정보를 갖고 있는 클래스, default -> type 클래스
                                        # metaclass=ABCMeta : 클래스가 특정 메서드를 구현하는지를 테스트 하는 기능

    @abstractmethod
    def Quack(self):
        pass

# 테스트