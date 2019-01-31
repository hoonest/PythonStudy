class ClassVar:
    text_list = []              # 클래스 멤버(인스턴스가 공유하는 멤버로 사용)

    def add(self, text):
        self.text_list.append(text)

    def print_list(self):
        print(self.text_list)

if __name__ == '__main__':
    a = ClassVar()
    a.add('a')
    a.print_list()