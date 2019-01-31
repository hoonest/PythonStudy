class Car:
    # 변수

    # 생성자
    def __init__(self):
        self.color = 0xFF0000       #차량색상
        self.wheel_size = 16        #바퀴의 크기
        self.displacement = 2000    #엔진 배기량

    # 메서드(함수)
    def forward(self):               # 전진
        pass

    def backward(self):             # 후진
        pass

    def turn_left(self):            # 좌회전
        pass

    def turh_right(self):
        pass

print(dir())        # 클래스 선언과 동시에 생성된 이름 공간의 확인(Car)
print(type(Car))    # 클래스 타입

print('__name__ : ', __name__)

if __name__ == '__main__':
    my_car = Car()          #Car 클래스의 객체 my_car 생성
    print('0x{:02X}'.format(my_car.color))

    print(my_car.wheel_size)
    print(my_car.displacement)

    my_car.forward()            # my_car 멤버메서드 접근 방법
    my_car.backward()
    my_car.turn_left()
    my_car.turh_right()

