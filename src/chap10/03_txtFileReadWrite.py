

lines = ["we'll find a way we always have - Interstellar\n",
         "I'll find you and I'll kill you - Taken\n",
         "I'll be back - Terminator 2\n"]

with open('movie_quotes.txt', 'w') as file:
    for line in lines:
        file.write(line)



with open('movie_quotes.txt', 'r') as file:
    line = file.readline()
    while line != '':
        print(line, end='')
        line = file.readline()

print('=========================')

with open('movie_quotes.txt', 'r') as file:
    lines = file.readlines()
    line = ''
    for line in lines:
        print(line, end ='')

