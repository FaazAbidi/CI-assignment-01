from enum import Enum
from EA import *
import random

class SelectionFunctions:
    """
    This class contains static methods of different fitness functions
    These functions takes list of tuples as population and
    returns their fitness scores as list of integers
    """

    @staticmethod
    def random(population: list, fitness_scores: list, select_count: int) -> list:
        """
        This method will select randomly two chromosomes from the population as selected_chromosome
        """
        assert len(population) == len(fitness_scores)
        assert select_count <= len(population)

        selected_chromosomes = random.sample(population,k=select_count)
        return selected_chromosomes

    
    @staticmethod
    def truncation(population: list, fitness_scores: list, select_count: int) -> list:
        """
        This method will select chromosomes with the highest fitness values from the population as selected_chromosome
        """
        assert len(population) == len(fitness_scores)
        assert select_count <= len(population)

        fitness_scores_copy = fitness_scores.copy()
        fitness_scores_copy.sort(reverse=True)
        selected_chromosome_index = [fitness_scores.index(value) for value in fitness_scores_copy[:select_count]]
        selected_chromosome = [population[index] for index in selected_chromosome_index]
        return selected_chromosome

    @staticmethod
    def proportional_selection(population: list, fitness_scores: list, select_count: int) -> list:
        """
        This method will select chromosomes by following the proportional selection approach
        """
        assert len(population) == len(fitness_scores)
        assert select_count <= len(population)

        normalized_values = [x/sum(fitness_scores) for x in fitness_scores]
        selected_chromosome = []
        
        # creating ranges for each chromosome using their normalized fitness scores
        ranges = [(0, normalized_values[0])]
        for i in range(len(normalized_values)-1):
            ranges.append((ranges[i][1], ranges[i][1]+normalized_values[i+1],))

        # generating random numbers between 0 and 1 and making sure that they doesn't lie in the same range
        # and selecting those who are in the range
        while len(selected_chromosome) < select_count:
            random_val = random.random()
            for i in range(len(ranges)):
                if random_val >= ranges[i][0] and random_val <= ranges[i][1] and population[i] not in selected_chromosome:
                    selected_chromosome.append(population[i])

        return selected_chromosome

    @staticmethod
    def rank_based_selection(population: list, fitness_scores: list, select_count: int) -> list:
        """
        In rank-based selection we will assign ranks and then normalize those ranks for creating 
        ranges.
        """
        assert len(population) == len(fitness_scores)
        assert select_count <= len(population)

        # assigning ranks to chromosomes
        fitness_scores_copy = fitness_scores.copy()
        fitness_scores_copy.sort()
        ranks = [fitness_scores_copy.index(x)+1 for x in fitness_scores]

        # normalizing ranks
        ranks = [x/sum(ranks) for x in ranks]

        # creating ranges for each chromosome using their normalized fitness scores
        ranges = [(0, ranks[0])]
        for i in range(len(ranks)-1):
            ranges.append((ranges[i][1], ranges[i][1]+ranks[i+1],))
        
        # generating random numbers between 0 and 1 and making sure that they doesn't lie in the same range
        # and selecting those who are in the range
        selected_chromosome = []
        while len(selected_chromosome) < select_count:
            random_val = random.random()
            for i in range(len(ranges)):
                if random_val >= ranges[i][0] and random_val <= ranges[i][1] and population[i] not in selected_chromosome:
                    selected_chromosome.append(population[i])
        
        return selected_chromosome


    @staticmethod
    def binary_tournament(population: list, fitness_scores: list, select_count: int) -> list:
        """
        This method will select two chromosomes from the population as selected_chromosome using binary tournament approach
        """
        assert len(population) == len(fitness_scores)
        assert select_count <= len(population)

        toarnament_size = 2
        selected_chromosome = []
        while len(selected_chromosome) < select_count:
            random_from_population = random.sample(population,k=toarnament_size)
            best_candidate = max(fitness_scores[population.index(random_from_population[0])], fitness_scores[population.index(random_from_population[1])])
            if population[fitness_scores.index(best_candidate)] not in selected_chromosome:
                selected_chromosome.append(population[fitness_scores.index(best_candidate)])

        return selected_chromosome