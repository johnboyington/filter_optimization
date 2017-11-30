from filter import Filter
from numpy.random import rand, randint
from material import test_library


class Operations(object):

    def __init__(self):
        self.set_params()

    def set_params(self):
        self.min_length = 3
        self.max_length = 20
        self.num_disc = 30
        self.num_mat = len(test_library.lib)

    def splice(self, child_ID, parent_1, parent_2):
        assert isinstance(parent_1, Filter), 'splicing requires Filter objects'
        assert isinstance(parent_2, Filter), 'splicing requires Filter objects'
        child_chrom = []
        for genome in range(len(parent_1.chromosome)):
            if rand() > 0.5:
                child_chrom += [parent_1.chromosome[genome]]
            else:
                child_chrom += [parent_2.chromosome[genome]]
        return Filter(child_ID, child_chrom)

    def mutate(self, individual):
        gene = randint(0, 30)
        assert isinstance(individual, Filter), 'mutating requires Filter objects'
        if gene == 1:
            new_gene = rand() * (self.max_length - self.min_length) + self.min_length
        else:
            new_gene = [randint(0, self.num_mat - 1)]
        chrom = individual.chromosome
        chrom[gene] = new_gene
        return Filter(individual.ID, chrom)

ops = Operations()
