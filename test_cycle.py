from population import Population


class Test_Cycle(object):

    def __init__(self, num_gens):
        self.num_generations = num_gens
        self.iterate()
        self.plot()

    def iterate(self):
        self.origin()
        for i in range(self.num_generations):
            self.cycle()
            self.plot()

    def origin(self):
        self.test = Population(10)
        self.test.init_current_gen()
        self.test.run_current_gen()
        self.test.sort_current_gen()

    def cycle(self):
        self.test.init_next_gen()
        self.test.run_current_gen()
        self.test.sort_current_gen()

    def plot(self):
        self.test.plot_current_gen()


if __name__ == '__main__':
    test = Test_Cycle(3)
