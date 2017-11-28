
from material import test_library


class Filter(object):

    def __init__(self, ID, chromosome):
        self.ID = ID
        assert type(chromosome) is list, 'chromosome must be of type list'
        self.chromosome = chromosome
        self.length = self.chromosome[0]
        self.materials = self.chromosome[1:]
        self.set_params()
        self.get_materials()

    def set_params(self):
        self.num_disc = 30

    def get_materials(self):
        self.material_bank = test_library.lib

    def write_neutron(self):
        default_text = open('neutron_template.i', 'r').read().split('*FLAG*')
        s = default_text[0]
        for d in range(self.num_disc):
            m = self.material_bank[self.materials[d]]
            args = [200 + d, m.num, -m.density, 130 + d, 131 + d, m.name]
            s += '{}  {} {:9.5f} 120 -121 122 -123  {} -{}   $ {}\n'.format(*args)
        s += default_text[1]
        s += '90 0 -32 #11 #12 #13 (-130:-120:121:-122:123:{}) #31\n'.format(130+self.num_disc)
        s += default_text[2]
        for d in range(self.num_disc):
            args = [131 + d, self.length * ((d + 1) / self.num_disc)]
            s += '{} PX  {:9.5f}\n'.format(*args)
        s += '41  PX  {:9.5f}     $ Detector\n'.format(self.length + 0.0002)
        s += default_text[3]
        s += 'IMP:n 1 {}r 0\n'.format(self.num_disc + 4)
        s += 'IMP:p 1 {}r 0\n'.format(self.num_disc + 4)
        s += default_text[4]
        for m in set(self.materials + [0, 1, 2, 3]):
            mat = self.material_bank[m]
            s += 'c  -----------------------------------------------------------------------------\n'
            s += 'c  MATERIAL  {:3d}: {}\n'.format(mat.num, mat.name)
            s += 'c  -------------------------------------(density {:8.5} g/cm^3)---------------\n'.format(mat.density)
            for i, comp in enumerate(mat.composition):
                if i == 0:
                    card = 'M{}'.format(mat.num)
                else:
                    card = '    '
                s += '{}      {}   {}\n'.format(card, comp[0], comp[1])
            s += 'c\n'
        s += default_text[5]
        with open('{}n.i'.format(self.ID), 'w+') as F:
            F.write(s)


if __name__ == '__main__':
    c = [10, 1, 2, 3, 2, 2, 1, 2, 1, 2, 3, 1, 2, 3, 1, 2, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1]
    indiv = Filter(0, c)
    indiv.write_neutron()
