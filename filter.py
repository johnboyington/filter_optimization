

class Filter(object):
    
    def __init__(self, chromosome):
        assert chromosome is list, 'chromosome must be of type list'
        self.chromosome = chromosome
    
    def write(self):
        pass