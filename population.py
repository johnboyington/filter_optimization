from filter import Filter
from numpy.random import rand, randint
import numpy as np
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
        self.mut_per_gen = 2
        self.max_population = 10

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

    def sort_current_gen(self):
        self.current_generation = sorted(self.current_generation, key=Filter.get_fitness)
        # calculate CDF
        pdf = []
        for i in self.current_generation:
            pdf.append(i.fitness)
        pdf = np.array(pdf)
        if len(pdf) > self.max_population:
            pdf = pdf[-self.max_population:]
        pdf = pdf / np.sum(pdf)
        cdf = []
        for i, p in enumerate(pdf):
            cdf.append(np.sum(pdf[:i+1]))
        self.cdf = cdf

    def select(self):
        r1 = rand()
        r2 = rand()
        found_1 = False
        found_2 = False
        for i, ind in enumerate(self.cdf):
            if r1 < ind and not found_1:
                parent_1 = self.current_generation[i]
                found_1 = True
            if r2 < ind and not found_2:
                parent_2 = self.current_generation[i]
                found_2 = True
            if found_1 and found_2:
                break
        return parent_1, parent_2

    def init_next_gen(self):
        for i in range(self.next_gen_size):
            self.next_generation += [ops.splice(self.historic_population, *self.select())]
            self.historic_population += 1
        for i in range(self.mut_per_gen):
            lucky = randint(0, len(self.next_generation) - 1)
            self.next_generation[lucky] = ops.mutate(self.next_generation[lucky])
        self.current_generation += self.next_generation
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
    test.sort_current_gen()
    p1, p2 = test.select()
    print(p1.ID, p2.ID)
    # test.plot_current_gen()
