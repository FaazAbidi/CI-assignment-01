from Problems.problem import Problem
from selection_functions import SelectionFunctions
from EA import *
import random


class KnapsackProblem(Problem):
    """
    This class will contain the chromosome and the fitness function
    """
    def __init__(self) -> None:
        self.data = {}
        self.weight_limit=-1
        self.__load_data()
        self.population = self.__generate_initial_population()
        self.fitness_scores = self.fitness_score()

    def __load_data(self):
        """
        This method will load data from the given dataset and convert it into in a suitable
        chromosone representation
        """
        nodes_and_points = {}
        file = open("KP_Dataset/low-dimensional/f10_l-d_kp_20_879", "r")
        for i, line in enumerate(file.readlines()):
            if i == 0:
                line = line.split()
                self.weight_limit = int(line[1])
            else:
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
            all_profits = list(self.data.keys())
            random.shuffle(all_profits)
            # print(all_cities)
            knapsack = []
            current_weight = 0
            while(current_weight < self.weight_limit):
                profit_i = all_profits.pop(0)
                knapsack.append(profit_i)
                current_weight += self.data[profit_i]

            random_population.append(knapsack)
        return random_population
    
    
    def fitness_score(self)-> list:
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
        total_profit = 0
        for profit in chromosome:
            total_profit += profit
        return total_profit
        