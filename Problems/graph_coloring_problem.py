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

        self.chromosome = []
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
        max_degree = max(len(item) for item in self.data.values())

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
            chromosome = [tuple(np.random.choice(range(256), size=3)) for i in range(len(self.adj_matrix))]
            random_population.append(chromosome)
        return random_population

    
        



        

