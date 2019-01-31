"""
# 파이썬의 예외 처리 구문1

    try:
        # 문제가 없을 경우 실행 할 코드
    except:
        # 문제가 생겼을 때 실행 할 코드


try:
    print(1 / 0)
except:
    print("예외가 발생했습니다.")
"""

"""
# 파이썬의 예외 처리 구문2
    try:
        # 문제가 없을 경우 실행 할 코드
    except 예외형식1:
        # 예외형식1 문제가 생겼을 때 실행 할 코드
    except 예외형식2:
        # 예외형식2 문제가 생겼을 때 실행 할 코드


my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요: ")
    index = int(input())
    print(my_list[index] / 0)
except IndexError:
    print("잘못된 첨자입니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
"""

"""
# 파이썬의 예외 처리 구문3
    try:
        # 문제가 없을 경우 실행 할 코드
    except 예외형식1 as e:
        # 예외형식1 문제가 생겼을 때 실행 할 코드
    except 예외형식2 as e:
        # 예외형식2 문제가 생겼을 때 실행 할 코드


my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요: ")
    index = int(input())
    print(my_list[index] / 0)
except IndexError as e:
    print("잘못된 첨자입니다. ({0})".format(e))
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다. ({0})".format(e))


my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요: ")
    index = int(input())
    print(my_list[index] / 0)
except IndexError as e:
    print("잘못된 첨자입니다. ({0})".format(e))
except :
    print("예외가 발생했습니다.")
"""

"""
# try절을 무사히 실행하면 만날 수 있는 else

    try:
        # 실행할 코드 블록
    except:
        # 예외 처리 코드 블록
    else:
        # except절을 만나지 않았을 경우 실행하는 코드 블록


my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요: ")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except Exception as e:
    print("예외가 발생했습니다. ({0})".format(e))
else :
    print("리스트의 요소 출력에 성공했습니다.")
"""

"""
# 반드시 실행되는 finally

    try:
        # 실행할 코드 블록
    except:
        # 예외 처리 코드 블록
    else:
        # except절을 만나지 않았을 경우 실행하는 코드 블록
    finally:
        # 예외 발생 여부에 상관없이 반드시 실행되는 코드 블럭

my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요: ")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except Exception as e:
    print("예외가 발생했습니다. ({0})".format(e))
finally :
    print("반드시 실행됩니다.")


my_list = [1, 2, 3]

try:
    print("첨자를 입력하세요: ")
    index = int(input())
    print("my_list[{0}]: {1}".format(index, my_list[index]))
except Exception as e:
    print("예외가 발생했습니다. ({0})".format(e))
else:
    print("리스트의 요소 출력에 성공했습니다.")
finally:
    print("반드시 실행됩니다.")
"""

"""
# Exception 클래스

    BaseException
        SystemExit
        Keyboardinterrupt
        GeneratorExit
        Exception
            ...
            ArithmeticError
                ZeroDivisionError
                ...

            LookupError
                IndexError
                ...
            ...

"""

my_list = [1, 2, 3]

try:
    print('첨자를 입력하세요')
    index = int(input())
    print(my_list[index]/0)
except IndexError as e:
    print("1) 잘못된 첨자입니다. ({0})".format(e))
except ZeroDivisionError as err:
    print('2) 0으로 나눌수 없습니다. ({0})'.format(err))
#except Exception as c:
#    print("3) 예외가 발생했습니다. ({0})".format(c))
else:
    print('정상 실행')
finally:
    print('finally')