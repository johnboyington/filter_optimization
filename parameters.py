from material import test_library


class Parameters(object):

    def __init__(self):
        self.start_size = 2100
        self.num_gens = 20
        self.min_length = 10
        self.max_length = 30
        self.num_disc = 10
        self.num_mat = len(test_library.lib)
        self.next_gen_size = self.start_size
        self.mut_per_gen = int(self.next_gen_size * 0.05)
        self.max_population = self.start_size

