import numpy as np
import matplotlib.pyplot as plt

class matplot:
    def test(self):
        x = np.arange(0, 6, 0.1)
        y = np.sin(x)

        plt.plot(x,y)
        plt.show()

    def test2(self):
        x = np.arange(0, 6, 0.1)
        y1 = np.sin(x)
        y2 = np.cos(x)

        plt.plot(x, y1, label = 'sin')
        plt.plot(x, y2, linestyle='--', label='cos')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title('sin & cos')
        plt.legend()
        plt.show()


    def AND(self, x1, x2):
        w1, w2, theta = 0.5, 0.5, 0.7
        tmp = x1*w1 + x2*w2
        if tmp <= theta:
            return 0
        elif tmp > theta:
            return 1



if __name__ == '__main__':
    mp = matplot()

    print(mp.AND(0, 0))
    print(mp.AND(0, 1))
    print(mp.AND(1, 0))
    print(mp.AND(1, 1))

    mp.test()
    mp.test2()
