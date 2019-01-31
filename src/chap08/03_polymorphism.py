# 다형성

class ArmorSuite:
    def armor(self):
        print('armored')

class IronMan(ArmorSuite):
    pass


def get_armored(suite):
    suite.armor()

if __name__ == '__main__':
    suite = ArmorSuite()
    get_armored(suite)
    # suite.armor()

    iron_man = IronMan()
    get_armored(iron_man)
