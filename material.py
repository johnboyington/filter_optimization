

class Material(object):

    def __init__(self, number, name, density, composition):
        self.num = number
        self.name = name
        self.density = density
        self.composition = composition


class Material_Library(object):

    def __init__(self, lib):
        self.lib = lib


mat_list = [\
            # borated polyethylene
            Material(1, 'Borated Polyethylene', 1.000, [('1001', -0.125355), ('5010.70c', -0.100000), ('6000', -0.774645)]),
            # lead
            Material(2, 'Lead', 11.34, [('82207.70c', -1.0)]),
            # tungsten
            Material(3, 'Tungsten', 19.3, [('074184', -1.0), ('13027.70c', -1.0)]),
            # new material
            Material(4, 'Cadmium', 8.65, [('048112', -1.0)])
            ]

test_library = Material_Library(mat_list)
