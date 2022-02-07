from Problems.problem import Problem
from selection_functions import SelectionFunctions
from EA import *
import random

class TSPProblem(Problem):
    """
    This class will contain the chromosome representation and  fitness function. This will also handle load data

    Constraints:
     - Not all cities are connected
     - Visit each city atleast once
     - Returns to the starting city
    """
    def __init__(self) -> None:
        self.data = {}
        self.__load_data()
        self.population = self.__generate_initial_population()
        self.fitness_scores = self.fitness_score()

    def __load_data(self):
        """
        This method will load data from the given dataset and convert it into in a suitable
        chromosone representation
        """
        nodes_and_points = {}
        file = open("TSP_dataset/qa194.tsp", "r")
        for line in file.readlines()[7:-1]:
            line = line.split()
            self.data[int(line[0])] = (float(line[1]), float(line[2]))
        file.close()


    def __generate_initial_population(self)-> list:
        """
        Every problem has its own generate_initial_population method 
        so we can have the option of implementing some other logic for it instead of always randomizing
        """
        all_cities = list(self.data.keys())
        random_population= []
        for element in range(population_size):
            random.shuffle(all_cities)
            # print(all_cities)
            random_population.append(all_cities.copy())
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
        total_distance = 0
        for i in range(len(chromosome)-1):
            total_distance += self.__distance(chromosome[i], chromosome[i+1])
        total_distance += self.__distance(chromosome[0], chromosome[-1])
        return total_distance


    def __distance(self, city1: int, city2: int)-> int:
        """
        This method will calculate the distance between two cities
        """
        return ((self.data[city1][0] - self.data[city2][0])**2 + (self.data[city1][1] - self.data[city2][1])**2)**0.5