import copy
import ea.genotype as genotype_class
import ea.log as log_class
import math
import puzzle.light_up_puzzle as puzzle_class
import random
import util.seed as seed_class


class MOEADriver:
    def __init__(self, config):
        """Initializes the MOEADriver class.
        
        Where config is a Config object. 
        """

        self.config = config

        # Initialize the seed class
        self.seed = seed_class.Seed(self.config)

        self.population_size = int(self.config.settings['mu'])
        self.offspring_pool_size = int(self.config.settings['lambda'])
        
        self.run_count = 1
        # self.best_fit_global_genotype = genotype_class.Genotype()
        # self.best_fit_global_genotype.fitness =  -1 * int(self.config.settings['arbitrary_large_number'])

        self.init_run_variables()

        # Initialize the log file class
        self.log = log_class.Log(self.config, self.seed, self.phenotype, overwrite=True)

        self.fronts = []


    def init_run_variables(self):
        """Initializes run specific variables.

        This function should be called before each run.
        """

        def force_adj_bulbs():
            """Places bulbs around black squares where there is only one valid
            bulb placement pattern.
            """
            bulbs = set([])

            # Determine where to place bulbs
            for black_square in self.phenotype.black_squares:
                # Get the adjacent coordinates to black_square that are not black
                adj_coords = [s for s in self.phenotype.get_adj_coords(black_square) if not s in self.phenotype.black_squares]

                if self.phenotype.black_squares[black_square] == len(adj_coords):
                    # There is only one way to place bulbs around this square
                    # Place those bulbs
                    for coord in adj_coords:
                        self.phenotype.place_bulb(coord, bulbs)
            
            # Save bulb placements to each genotype
            for genotype in self.population:
                genotype.bulbs = copy.deepcopy(bulbs)


        def init_puzzles_with_bulbs():
            """Randomly places bulbs on each puzzle in population in a uniform manner.
            
            The number of attempted bulb placement failures is determined by config.
            """
            for genotype_index in range(len(self.population)):
                # Place bulbs until num_bulb_placement_failures failures are reached
                failure_count = 0
                while failure_count < int(self.config.settings['num_bulb_placement_failures']):
                    if not self.phenotype.place_bulb_randomly(self.population[genotype_index].bulbs):
                        failure_count += 1
                    else:
                        break

        self.total_bulb_shine_ratio_sum = 0.0
        self.total_black_cell_constraints_violated = 0
        self.total_bulb_shine_constraints_violated = 0

        self.total_genotypes_seen = 0

        self.avg_bulb_shine_ratio = 0.0
        self.avg_black_cell_constraints_violated = 0.0
        self.avg_bulb_shine_constraints_violated = 0.0

        self.local_best_shine_ratio = 0.0
        self.local_best_bulb_shine_constraints = int(self.config.settings['arbitrary_large_number'])
        self.local_best_black_cell_constraints = int(self.config.settings['arbitrary_large_number'])

        self.eval_count = 0

        # Create/reset the base puzzle class (phenotype)
        self.phenotype = puzzle_class.LightUpPuzzle(self.config)

        # Create/reset the puzzle population: a list genotypes
        self.population = []
        for _ in range(self.population_size):
            self.population.append(genotype_class.Genotype(self.config))

        self.parents = []
        self.children = []

        if int(self.config.settings['force_validity']):
            # Use black square adjacency heuristic to force validity
            force_adj_bulbs()
        
        init_puzzles_with_bulbs()

    
    def evaluate(self, genotypes, log_run=True):
        """Evaluates all genotypes in the list genotypes, updating their fitness values, the average 
        fitness value, and the best fitness seen so far.

        If log_run is True, the state of the experiment is written to the log file.
        """ 

        def set_fitnesses_to_level_number():
            """Updates each genotype's fitness to be its level in the Pareto fronts."""
            for front_index, front in enumerate(self.fronts):
                for genotype in front:
                    genotype.fitness = front_index + 1


        for genotype in genotypes:
            self.phenotype.get_fitness(genotype)
            self.determine_domination()
            set_fitnesses_to_level_number()

            # TODO: Update soln file w/ new constraints

            # Calculate average subfitnesses
            self.total_bulb_shine_ratio_sum += genotype.shine_ratio
            self.total_black_cell_constraints_violated += genotype.black_cell_constraints_violated
            self.total_bulb_shine_constraints_violated += genotype.bulb_shine_constraints_violated

            self.total_genotypes_seen += 1

            self.avg_bulb_shine_ratio = genotype.shine_ratio / self.total_genotypes_seen
            self.avg_black_cell_constraints_violated = genotype.black_cell_constraints_violated / self.total_genotypes_seen
            self.avg_bulb_shine_constraints_violated = genotype.bulb_shine_constraints_violated / self.total_genotypes_seen

            # Determine new local best subfitnesses
            self.local_best_shine_ratio = max(genotype.shine_ratio, self.local_best_shine_ratio)
            self.local_best_black_cell_constraints = min(genotype.black_cell_constraints_violated, self.local_best_black_cell_constraints)
            self.local_best_bulb_shine_constraints = min(genotype.bulb_shine_constraints_violated, self.local_best_bulb_shine_constraints)

            # if genotype.fitness > self.best_fit_local_genotype.fitness:
            #     self.best_fit_local_genotype = genotype

            #     if self.best_fit_local_genotype.fitness > self.best_fit_global_genotype.fitness:
            #         self.best_fit_global_genotype = self.best_fit_local_genotype

            #         # Write to solution file
            #         self.phenotype.write_to_soln_file(self.best_fit_global_genotype.bulbs)

            #         # Visualize the solution
            #         if int(self.config.settings['visualize_best_solution']):
            #             self.phenotype.write_to_soln_visualization_file(self.best_fit_global_genotype.bulbs)

            # Determine if the population fitness is stagnating
            # if math.isclose(self.avg_fitness, self.prev_avg_fitness_termination, rel_tol=float(self.config.settings['termination_convergence_criterion_magnitude'])):
            #     self.stale_fitness_count_termination += 1
            # else:
            #     self.stale_fitness_count_termination = 0
            #     self.prev_avg_fitness_termination = self.avg_fitness
            
            # if math.isclose(self.avg_fitness, self.prev_avg_fitness_mutation, rel_tol=float(self.config.settings['mutation_factor_criterion_magnitude'])):
            #     self.stale_fitness_count_mutation += 1
            # else:
            #     self.stale_fitness_count_mutation = 0
            #     self.prev_avg_fitness_mutation = self.avg_fitness
            
            self.eval_count += 1

        if log_run:
            self.log.write_run_data(self.eval_count, self.avg_bulb_shine_ratio, self.local_best_shine_ratio, self.avg_bulb_shine_constraints_violated, 
                self.local_best_bulb_shine_constraints, self.avg_black_cell_constraints_violated, self.local_best_black_cell_constraints)


    def select_parents(self):
        """Chooses which parents from the population will breed.

        Depending on the parent selection configuration, one of the three following methods
        is used to select parents:
            1. Uniform random selection
            2. Fitness proportional selection
            3. k-tournament selection with replacement

        The resulting parents are stored in self.parents.
        """
        self.parents = []
        parent_population_size = int(self.config.settings['parent_population_size'])

        if int(self.config.settings['use_uniform_random_parent_selection']):
            # Select parents using a uniform random approach
            tmp_population = self.population
            random.shuffle(tmp_population)

            self.parents = tmp_population[:parent_population_size]

        elif int(self.config.settings['use_fitness_proportional_parent_selection']):
            # Select parents for breeding using the fitness proportional "roulette wheel" method (with replacement)
            self.parents = random.choices(self.population, weights=[1 / abs(g.fitness) for g in self.population], k=parent_population_size)

        else:
            # Perform a k-tournament selection with replacement
            while len(self.parents) <= parent_population_size:
                self.parents.append(self.perform_tournament_selection(self.population, int(self.config.settings['k_parent_selection']), w_replacement=True))
            
            # Maintain the parent population size
            # This accounts for situations where the parent population size is not divisible by k
            self.parents = self.parents[:parent_population_size]


    def recombine(self):
        """Breeds lambda (offspring_pool_size) children from the existing parent population.

        The resulting children are stored in self.children.
        """

        def breed(parent_a, parent_b):
            """Breeds two parent genotypes together to produce a child genotype using
            n-point crossover.

            Returns the child genotype.
            """
            a_bulbs = list(parent_a.bulbs)
            b_bulbs = list(parent_b.bulbs)

            # Perform a n-point crossover on the parent's bulbs
            n = int(self.config.settings['n_point_crossover'])

            min_crossover_index = 0
            max_crossover_index = min(len(a_bulbs) - 1, len(b_bulbs) - 1)

            if not max_crossover_index:
                if len(parent_a.bulbs):
                    return genotype_class.Genotype(self.config, parent_a.bulbs)
                else:
                    return genotype_class.Genotype(self.config, parent_b.bulbs)

            crossover_indices = []
            rand_start = min_crossover_index 
            for _ in range(n):
                if not rand_start == max_crossover_index and rand_start < max_crossover_index:
                    crossover_indices.append(random.randint(rand_start, max_crossover_index))
                    rand_start = crossover_indices[-1]
            
            # Ensure the entire parent is copied during crossover
            crossover_indices.append(max_crossover_index + 1)

            child_bulbs = set([])
            prev_crossover_index = 0
            for crossover_index in crossover_indices:
                if random.random() < float(self.config.settings['parent_selection_weight']):
                    # Choose parent_a's substring
                    for bulb in a_bulbs[prev_crossover_index:crossover_index]:
                        child_bulbs.add(bulb)

                else:
                    # Choose parent_b's substring
                    for bulb in b_bulbs[prev_crossover_index:crossover_index]:
                        child_bulbs.add(bulb)
                
                prev_crossover_index = crossover_index
            
            return genotype_class.Genotype(self.config, child_bulbs)


        self.children = []

        for _ in range(self.offspring_pool_size):
            # Select parents with replacement
            # Note: this implementation allows for parent_a and parent_b to be the same genotype
            parent_a = self.parents[random.randint(0, len(self.parents) - 1)]
            parent_b = self.parents[random.randint(0, len(self.parents) - 1)]

            # Produce a child
            self.children.append(breed(parent_a, parent_b))
        
    
    def mutate(self):
        """Probabilistically performs mutation on each child in the child population."""

        def shuffle_bulb(child):
            """Attempts to move the placement of a random bulb to a random position in a given
            child genotype.

            If this cannot be done in a valid way, the child's bulb is removed.
            """
            if random.random() < mutation_probability:
                for _ in range(int(self.config.settings['num_bulb_removals_mutation'])):
                    try:
                        child.bulbs.pop()
                    except:
                        # The bulbs set is empty
                        break
            
            fail_count = 0
            while fail_count < int(self.config.settings['num_bulb_placement_failures_mutation']):
                if self.phenotype.place_bulb_randomly(child.bulbs):
                    break
                else:
                    fail_count += 1


        mutation_probability = float(self.config.settings['mutation_probability'])

        # Determine if the stagnant population fitness requires more mutation
        # if self.stale_fitness_count_mutation >= int(self.config.settings['mutation_factor_criterion']):
        #     # There has been no change in average fitness for too long
        #     mutation_probability *= float(self.config.settings['mutation_scale_factor'])

        for child in self.children:
            if random.random() < mutation_probability:
                for i in range(random.randint(1, int(self.config.settings['rand_num_bulb_shuffles']))):
                    shuffle_bulb(child)


    def select_for_survival(self):
        """For comma survival strategy:
            Kills the previous self.population and selects for survival from the self.children population while keeping
            mu (population size) constant.
        
        For plus survival strategy:
            Integrates children from self.children into self.population while keeping mu constant.
        
        Note: The survival strategy can be configured in config.        

        Depending on the survival selection configuration, one of the four following methods
        is used to select survivors:
            1. Uniform random selection
            2. Truncation
            3. Fitness proportional selection
            4. k-tournament selection without replacement
        """
        if int(self.config.settings['use_comma_survival_strategy']):
            # Use the comma survival strategy
            selection_pool = self.children
        else:
            # Default to using the plus survival strategy
            selection_pool = self.population + self.children
            
        self.population = []

        if int(self.config.settings['use_uniform_random_survival_selection']):
            # Select offspring for survival using a uniform random approach
            tmp_selection_pool = selection_pool
            random.shuffle(tmp_selection_pool)

            self.population = tmp_selection_pool[:self.population_size]

        elif int(self.config.settings['use_truncation']):
            # Use truncation for survival selection
            self.sort_genotypes(selection_pool)
            self.population = selection_pool[:self.population_size]

        elif int(self.config.settings['use_fitness_proportional_survival_selection']):
            # Select offspring for survival using the fitness proportional "roulette wheel" method (with replacement)
            self.population = random.choices(selection_pool, weights=[1 / abs(g.fitness) for g in selection_pool], k=self.population_size)
        
        else:
            # Use k-tournament for survival selection without replacement
            while len(self.population) <= self.population_size:
                self.population.append(self.perform_tournament_selection(selection_pool, int(self.config.settings['k_survival_selection']), w_replacement=False))

            # Maintain the population size
            # This accounts for situations where the population size is not divisible by k
            self.population = self.population[:self.population_size]


    def decide_termination(self):
        """Returns True if the program will terminate, False otherwise.

        The program will terminate if any of the following conditions are True:
            1. There has been no change in fitness (average fitness) for n evaluations.
            2. The number of evaluations specified in config has been reached.
        """
        # if self.stale_fitness_count_termination >= int(self.config.settings['n_termination_convergence_criterion']):
        #     # There has been no change in average fitness for too long
        #     return True

        if self.eval_count >= int(self.config.settings['num_fitness_evaluations']):
            # The number of desired evaluations has been reached
            return True

        return False


    def sort_genotypes(self, genotype_list):
        """Sorts the given genotype list from most fit to least fit by each
        element's fitness ratio.
        """
        genotype_list.sort(key=lambda x : x.fitness)


    def increment_run_count(self):
        """Increments the run count by one."""
        self.run_count += 1

    
    def perform_tournament_selection(self, genotypes, k, w_replacement=False):
        """Performs a k-tournament selection on genotypes, a list of genotype objects.

        Returns the winning genotype.
        """
        arena_genotypes = []
        forbidden_indices = set([])

        # Randomly select k elements from genotypes
        for _ in range(k):
            rand_index = random.randint(0, len(genotypes) - 1)

            # Don't allow replacement (if applicable)
            while rand_index in forbidden_indices:
                rand_index = random.randint(0, len(genotypes) - 1)

            arena_genotypes.append(genotypes[rand_index])

            if w_replacement == False:
                forbidden_indices.add(rand_index)

        # Make the genotypes fight, return the winner
        return max(arena_genotypes, key=lambda x : x.fitness)


    def determine_domination(self):
        """Generates a transient domination table and uses it to produce and return
        front classifications in the form of TODO SOME DATA STRUCTURE.
        """

        def better(genotype_a, genotype_b):
            """Returns True if genotype_a dominates genotype_b, False otherwise."""
            return genotype_a.fitness >= genotype_b.fitness \
                and genotype_a.black_cell_constraints_violated <= genotype_b.black_cell_constraints_violated \
                and genotype_a.bulb_shine_constraints_violated <= genotype_b.bulb_shine_constraints_violated \
                and (genotype_a.fitness > genotype_b.fitness \
                or genotype_a.black_cell_constraints_violated < genotype_b.black_cell_constraints_violated \
                or genotype_a.bulb_shine_constraints_violated < genotype_b.bulb_shine_constraints_violated)
        

        def adjust_fronts(fronts, front_index, new_genotype):
            """Recursively percolates genotypes down in fronts starting at level front_index if genotypes 
            in that level are dominated by new_genotype.

            Modifies fronts in place.
            """
            if front_index >= len(fronts):
                # Add new_genotype to a new level in fronts
                fronts.append([new_genotype])
            
            else:
                # Add new_genotype to this front
                fronts[front_index].append(new_genotype)

                tmp_fronts = fronts[front_index][:-1]

                # Compare added genotype to the genotypes in this front (not comparing new_genotype to itself)
                for genotype_to_compare in tmp_fronts:
                    if better(new_genotype, genotype_to_compare):
                        # genotype_to_compare doesn't belong in this level, adjust it
                        try:
                            fronts[front_index].remove(genotype_to_compare)
                        except:
                            pass

                        adjust_fronts(fronts, front_index + 1, genotype_to_compare)


        # Create the domination table
        # TODO: These calculations can be optimized for time

        for dominating_genotype in self.population:
            dominating_genotype.dominates = []

            for dominated_genotype in self.population:
                if better(dominating_genotype, dominated_genotype):
                    dominating_genotype.dominates.append(dominating_genotype)
        
        # Create the Pareto fronts (levels of domination)
        self.fronts = []

        for genotype_to_add in self.population:
            if self.fronts:
                # Determine the next element placement
                for index, level in enumerate(self.fronts):
                    index_to_place = -1
                    genotype_to_add_is_dominated = False

                    for genotype in level:
                        if better(genotype, genotype_to_add):
                            genotype_to_add_is_dominated = True
                            break
                    
                    if not genotype_to_add_is_dominated:
                        # Add the genotype to this level and break out
                        index_to_place = index
                        break
                
                if index_to_place < 0:
                    # Add the genotype to a new front
                    adjust_fronts(self.fronts, len(self.fronts), genotype_to_add)

                else:
                    # Adjust elements in the updated front
                    adjust_fronts(self.fronts, index_to_place, genotype_to_add)

            else:
                # Add the 0th element
                self.fronts.append([genotype_to_add])

        return self.fronts
