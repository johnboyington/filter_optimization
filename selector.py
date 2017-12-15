import numpy as np
from filter import Filter


class Selector(object):

    def __init__(self, ft, ng):
        self.ft_constraint = ft
        self.ng_constraint = ng
        self.load_data()
        # self.constrain_ft()
        self.constrain_ng()
        self.make_best()

    def load_data(self):
        self.data = np.loadtxt('data.txt')

    def constrain_ft(self):
        new = []
        for f in self.data:
            if 1 > f[1] > self.ft_constraint:
                new.append(f)
        new = sorted(new, key=lambda x: x[2])
        print(new[-1])
        self.best_chrom = new[-1]

    def constrain_ng(self):
        new = []
        for f in self.data:
            if f[2] > self.ng_constraint and f[1] != 1:
                new.append(f)
        new = sorted(new, key=lambda x: x[1])
        print(new[-1])
        best_filter = new[-1]
        self.best_chrom = []
        for i, gene in enumerate(best_filter[4:]):
            if i == 0:
                self.best_chrom.append(float(gene))
            else:
                self.best_chrom.append(int(gene))

    def make_best(self):
        self.best = Filter(1, self.best_chrom)
        self.best.write()


if True:
    Selector(0.9, 1)
