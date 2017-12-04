import matplotlib.pyplot as plt
import numpy as np


class Plot(object):

    def __init__(self):
        self.get_data()
        self.plot_legacy()
        self.plot_ratios()

    def get_data(self):
        n = 5
        g = 32
        self.data = np.loadtxt('data.txt').reshape(n, g, -1)

    def plot_legacy(self):
        plt.figure(30)
        for n, i in enumerate(self.data):
            i = i.T
            plt.plot(range(32), i[0], marker='o', label='gen {}'.format(n))
        plt.xlabel('Individual (Ordered by Fitness)')
        plt.ylabel('Fitness')
        plt.legend()
        plt.savefig('legend.png', dpi=250)

    def plot_ratios(self):
        plt.figure(31)
        for i, n in enumerate(self.data):
            ft = []
            ng = []
            for nn in n:
                ft.append(nn[1])
                ng.append(nn[2])
            plt.plot(ft, ng, linestyle='none', marker='o', label='gen {}'.format(i))
        plt.xlabel('Fast to Total Ratio')
        plt.ylabel('Neutron to Gamma Ratio')
        plt.legend()
        plt.savefig('ratios.png', dpi=250)


if __name__ == '__main__':
    plot = Plot()