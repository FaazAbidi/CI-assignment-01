from sympy import are_similar
from Problems.problem import Problem
from selection_functions import SelectionFunctions
from EA import *
import random
import numpy as np

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

        num_keys = len(self.edges.keys())
        self.data['num_keys'] = num_keys
        max_degree = max(len(item) for item in self.data.keys())
        self.data['max_degree'] = max_degree 

        for i in range(num_keys):
            self.adj_matrix.append([0 for i in range(num_keys)])
        
        for key in self.edges:
            for nodes in self.edges[key]:
                self.adj_matrix[key-1][nodes-1] = 1
                self.adj_matrix[nodes-1][key-1] = 1
        
    def __generate_initial_population(self)-> list:
        """
        random generation
        """
        random_population = []
        for element in range(POPULATION_SIZE):
            chromosome = []
            for i in range(self.data['num_keys']):
                np.random.seed()
                color = random.randint(0, self.data['max_degree']*4)
                gene = (color, color, color)
                chromosome.append(gene)
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

    def __fitness_function(self, chromosome: list)-> int:
        """
        This method will calculate the fitness of the chromosome
        """
        fitness = 0
        for key in self.edges:
            for nodes in self.edges[key]:
                if chromosome[key-1] == chromosome[nodes-1]:
                    fitness +=1
        return -fitness

    def crossover(self, parent1: list, parent2: list) -> list:
        """
        This method will perform one point crossover 
        We have eliminated the possibility of wrong chromosomes. 
        """
        crossover_point = random.randint(0, len(parent1)-1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutation(self, child: list, mutation_rate: float()) -> list:
        """
        For the mutation, we will reassign a random gene with the value of an existing gene
        """
        random_val = random.random()
        if random_val < mutation_rate:
            random_index_1 = random.randint(0,len(child)-1) 
            random_index_2 = random.randint(0,len(child)-1) 
            child[random_index_1] = child[random_index_2]
        return child
    
    


    
        



        

