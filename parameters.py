from material import test_library


class Parameters(object):

    def __init__(self):
        self.start_size = 98
        self.num_gens = 5
        self.min_length = 3
        self.max_length = 20
        self.num_disc = 30
        self.num_mat = len(test_library.lib)
        self.next_gen_size = self.start_size
        self.mut_per_gen = 5
        self.max_population = self.start_size
