from filter import Filter
from numpy.random import rand, randint
from material import test_library
from operations import ops
import matplotlib.pyplot as plt


class Population(object):

    def __init__(self, initial_pop):
        self.initial_population = initial_pop
        self.set_params()
        self.current_generation = []
        self.historic_population = 0
        self.next_generation = []

    def set_params(self):
        self.min_length = 3
        self.max_length = 20
        self.num_disc = 30
        self.num_mat = len(test_library.lib)
        self.next_gen_size = 10
        self.children_per_crossover = 2

    def spawn_random(self, ID):
        chrom = []
        length = rand() * (self.max_length - self.min_length) + self.min_length
        chrom += [length]
        for mat in range(self.num_disc):
            chrom += [randint(0, self.num_mat - 1)]
        print(chrom)
        return Filter(ID, chrom)

    def init_current_gen(self):
        for i in range(self.initial_population):
            self.current_generation += [self.spawn_random(self.historic_population)]
            self.historic_population += 1

    def run_current_gen(self):
        for ind in self.current_generation:
            if ind.fitness == -1:
                ind.run_local()

    def init_next_gen(self):
        # TODO: finish this fucntion
        for i in range(self.initial_population):
            self.next_generation += [self.spawn_random(self.historic_population)]
            self.historic_population += 1
        return

    def plot_current_gen(self):
        ids = range(len(self.current_generation))
        fitnesses = []
        for i in ids:
            fitnesses.append(self.current_generation[i].fitness)
        plt.figure(10)
        plt.plot(ids, fitnesses, 'ko')
        plt.show()


if __name__ == '__main__':
    test = Population(4)
    test.init_current_gen()
    test.run_current_gen()
    test.plot_current_gen()
