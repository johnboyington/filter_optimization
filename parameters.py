from material import test_library


class Parameters(object):

    def __init__(self):
        self.start_size = 50
        self.num_gens = 9
        self.min_length = 3
        self.max_length = 20
        self.num_disc = 30
        self.num_mat = len(test_library.lib)
        self.next_gen_size = self.start_size
        self.mut_per_gen = int(self.next_gen_size * 0.05)
        self.max_population = self.start_size

