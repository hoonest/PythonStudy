
iterator = range(3).__iter__()

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

print('=============================')

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return  current
        else:
            raise StopIteration()


if __name__ == '__main__':
    for i in MyRange(0, 5):
        print(i)