from Problems.problem import Problem
from selection_functions import SelectionFunctions

# Global Parameters
population_size = 30
offspring_size = 10
generations = 100
mutation_rate = 0.5
iterations = 10

class EA:
    """
    This class will be a generic one. This will contain the evolutionary process
    """
    def __init__(self, problem: Problem):
        self.problem = problem
        self.population = self.problem.population
        self.fitness_scores = self.problem.fitness_scores
        self.generation = 1

    def generate_offspring(self):
        """
        This method will generate offspring from the population
        """
        # parents = SelectionFunctions.random(population=self.population, fitness_scores=self.fitness_scores, select_count=offspring_size)
        # parents = SelectionFunctions.truncation(population=self.population, fitness_scores=self.fitness_scores, select_count=offspring_size)
        parents = SelectionFunctions.proportional_selection(population=self.population, fitness_scores=self.fitness_scores, select_count=offspring_size)
        # parents = SelectionFunctions.rank_based_selection(population=self.population, fitness_scores=self.fitness_scores, select_count=offspring_size)
        # parents = SelectionFunctions.binary_tournament(population=self.population, fitness_scores=self.fitness_scores, select_count=offspring_size)
        
        



