# 인자이름의 올바른 사용예

def print_string1(text, count):
    for i in range(count):
        print(text)

print_string1('안녕하세요', 3)


# 기본값 인자(Default Argument Value)
def print_string2(text, count=1):
    for i in range(count):
        print(text)

print_string2('안녕하세요2')
print_string2('안녕하세요3', 5)
