# file 생성해서 write 하기.

file = open("test.txt", 'w')
file.write("hello")
file.close()


# file에서 읽어오기
file = open("test.txt", 'r')
str = file.read()
file.close()

print(str)






