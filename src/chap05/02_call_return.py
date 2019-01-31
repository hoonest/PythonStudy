def my_abs(arg):
    if (arg < 0):
        result = arg * -1
    else:
        result = arg

    return  result



print(my_abs(-5))
print(my_abs)  # 정의된 함수의 할당된 주소값 반환

print(globals())