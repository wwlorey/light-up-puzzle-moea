import copy


class Genotype:
    def __init__(self, config, bulbs=None):
        """Initializes the Genotype class."""
        if bulbs:
            self.bulbs = copy.deepcopy(bulbs)
        else:
            self.bulbs = set([])

        self.fitness = int(config.settings['arbitrary_large_number'])
        self.shine_ratio = 0.0
        self.black_cell_constraints_violated = 0
        self.bulb_shine_constraints_violated = 0
    