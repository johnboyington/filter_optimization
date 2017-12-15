import numpy as np


class Selector(object):

    def __init__(self, ft, ng):
        self.ft_constraint = ft
        self.ng_constraint = ng
        self.load_data()
        #self.constrain_ft()
        self.constrain_ng()

    def load_data(self):
        self.data = np.loadtxt('data.txt')

    def constrain_ft(self):
        new = []
        for f in self.data:
            if f[1] > self.ft_constraint:
                new.append(f)
        new = sorted(new, key=lambda x: x[2])
        print(new[-1])

    def constrain_ng(self):
        new = []
        for f in self.data:
            if f[2] > self.ng_constraint:
                new.append(f)
        new = sorted(new, key=lambda x: x[1])
        print(new[-1])
        for i in new[-1]:
            print(i)

if True:
    Selector(0.9, 1)
