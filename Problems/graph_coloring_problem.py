from scipy import rand
from sklearn.utils import check_array
from Problems.problem import Problem
from selection_functions import SelectionFunctions
from EA import *
import random
import numpy as np
import more_itertools as mit

from test import check_chromosome

class GC(Problem):
    """
    This class will contain chromosome representation of this particular problem 
    and its fitness functions
    """

    def __init__(self):

        self.data = {}
        self.edges = {}
        self.adj_matrix = []
        self.__load_data()
        self.population = self.__generate_initial_population()
        self.fitness_scores = self.fitness_score()

    def __load_data(self):
        """
        This method will load data from the given dataset and convert it into in a suitable
        chromosone representation
        """
        file = open("GC_Dataset/gcol1.txt", "r")
        for line in file.readlines()[1:-1]:
            line = line.split()
            if int(line[1]) in self.edges:
                self.edges[int(line[1])].append(int(line[2]))
            else:
                self.edges[int(line[1])] = []
                self.edges[int(line[1])].append(int(line[2]))

            if int(line[2]) in self.edges:
                self.edges[int(line[2])].append(int(line[1]))
            else:
                self.edges[int(line[2])] = []
                self.edges[int(line[2])].append(int(line[1]))
        file.close()

        num_keys = len(self.edges.keys())
        self.data['num_keys'] = num_keys
        max_degree = max(len(item) for item in self.edges.values())
        self.data['max_degree'] = max_degree

        for i in range(num_keys):
            self.adj_matrix.append([0 for i in range(num_keys)])

        for key in self.edges:
            for nodes in self.edges[key]:
                self.adj_matrix[key-1][nodes-1] = 1

    def __generate_initial_population(self) -> list:
        """
        random generation
        """
        random_population = []
        for element in range(POPULATION_SIZE):
            chromosome = []
            for i in range(self.data['num_keys']):
                flag = True
                while flag:
                    np.random.seed()
                    color = random.randint(0, self.data['max_degree']*2)
                    # RGB
                    gene = (color, color, color)
                    if gene not in chromosome:
                        chromosome.append(gene)
                        flag = False
                    else:
                        continue
            random_population.append(chromosome)
        return random_population

    def fitness_score(self) -> list:
        """
        This method will calculate the fitness score of the population
        """
        fitness_score = []
        for chromosome in self.population:
            fitness_score.append(self.__fitness_function(chromosome))
        return fitness_score

    def __fitness_function(self, chromosome: list) -> int:
        """
        This method will calculate the fitness of the chromosome
        """
        return -len(set(chromosome))

    # checks if the chromosome is a viable solution
    def check_chromosome(self, chromosome:list) -> bool:
        # iterates over all the color of each node
        for i in range(len(chromosome)):
            # iterates over all adjacent nodes
            for j in self.edges[i + 1]:
                if chromosome[i] == chromosome[j-1] and self.adj_matrix[i] == self.adj_matrix[j-1]:
                    return False   
        return True

    def crossover(self, parent1: list, parent2: list) -> list:
        """
        This method will perform two point crossover 
        We have eliminated the possibility of wrong chromosomes. 
        """
        
        for i in range(500):
            crossover_point_1 = random.randint(0, len(parent1))
            crossover_point_2 = random.randint(0, len(parent1))
            if crossover_point_1 < crossover_point_2:
                child = parent1[:crossover_point_1] + parent2[crossover_point_1:crossover_point_2] + parent1[crossover_point_2:]
            elif crossover_point_1 > crossover_point_2:
                child = parent1[:crossover_point_2] + parent2[crossover_point_2:crossover_point_1] + parent1[crossover_point_1:]
            else:
                child = parent1[:crossover_point_1] + parent2[crossover_point_1:]
            check = check_chromosome(child)
            if check:
                return child
        a = [parent1, parent2]
        random.shuffle(a)
        return a[0]

    def mutation(self, child: list, mutation_rate: float()) -> list:
        """
        For the mutation, we will reassign a random gene with the value of an existing gene
        """
        random_value = random.random()
        if random_value < mutation_rate:
            c = child
            ri_1 = random.randint(0, len(c)-1)
            ri_2 = random.randint(0, len(c)-1)
            c[ri_1] = c[ri_2]
            check = check_chromosome(c)
            if check:
                return c
        return child



        
            


