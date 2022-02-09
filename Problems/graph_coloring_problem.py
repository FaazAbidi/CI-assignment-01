from Problems.problem import Problem
from selection_functions import SelectionFunctions
from EA import *
import random
import numpy as np

class GraphColoringProblem(Problem):
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
        max_degree = max(len(item) for item in self.data.values())
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
            np.random.seed()
            chromosome = [tuple(np.random.choice(range(self.data['max_degree']), size=3)) for i in range(len(self.adj_matrix))]
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
                if chromosome[key+1] == chromosome[nodes+1]:
                    fitness +=1
        return fitness

    


    
        



        

