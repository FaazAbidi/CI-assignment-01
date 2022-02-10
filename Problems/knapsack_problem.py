from Problems.problem import Problem
from selection_functions import SelectionFunctions
from EA import *
import random
import numpy as np



class KnapsackProblem:
    """
    This class will contain the chromosome and the fitness function
    """
    def __init__(self):
        self.data = {}
        self.__load_data()
        self.population = self.__generate_initial_population()
        self.fitness_scores = self.fitness_score()

    def __load_data(self):
        """
        This method will load data from the given dataset and convert it into in a suitable
        chromosone representation
        """
        
        file = open("KS_Dataset/f2_l-d_kp_20_878.txt", "r")
        first_line = file.readline()
        self.data['total_items'] = first_line.split()[0]
        self.data['max_capacity'] = first_line.split()[1]
        for line in file.readlines()[1:-1]:
            line = line.split()
            self.data[int(line[0])] = int(line[1])
        file.close()
    
    def __generate_initial_population(self)-> list:
        """
        Every problem has its own generate_initial_population method 
        so we can have the option of implementing some other logic for it instead of always randomizing
        """
        random_population = []
        for element in range(POPULATION_SIZE):
            chromosome = [random.randint(0,10) for i in range(self.data['total_items'])]
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

        

            
    
