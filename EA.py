from Problems.problem import Problem
from selection_functions import SelectionFunctions
from reproductive_functions import ReproductiveFunctions
from enum import Enum

# Global Parameters
POPULATION_SIZE = 100
OFFSPRING_SIZE = 30  # offspring size must be a multiple of 2 (even)
GENERATIONS = 500
MUTATION_RATE = 0.2
ITERATIONS = 10


class Selection(Enum):
    """
    This class will contain the different selection functions
    """
    Random = 1
    Truncation = 2
    ProportionalSelection = 3
    RankBasedSelection = 4
    BinaryTournament = 5


class EA:
    """
    This class will be a generic one. This will contain the evolutionary process
    """
    def __init__(self, problem: Problem):
        self.problem = problem
        self.population = self.problem.population
        self.fitness_scores = self.problem.fitness_scores
        self.generation = 1

    def generate_offspring(self, selection: Selection):
        """
        This method will generate offspring from the population
        """
        # Selecting the fittest chromosomes
        if selection == Selection.Random:
            parents = SelectionFunctions.random(self.population, self.fitness_scores, OFFSPRING_SIZE)
        elif selection == Selection.Truncation:
            parents = SelectionFunctions.truncation(self.population, self.fitness_scores, OFFSPRING_SIZE)
        elif selection == Selection.ProportionalSelection:
            parents = SelectionFunctions.proportional_selection(self.population, self.fitness_scores, OFFSPRING_SIZE)
        elif selection == Selection.RankBasedSelection:
            parents = SelectionFunctions.rank_based_selection(self.population, self.fitness_scores, OFFSPRING_SIZE)
        elif selection == Selection.BinaryTournament:
            parents = SelectionFunctions.binary_tournament(self.population, self.fitness_scores, OFFSPRING_SIZE)
        
        for i in range(0,OFFSPRING_SIZE,2):
            child1 = ReproductiveFunctions.crossover(parent1=parents[i], parent2=parents[i+1])
            child2 = ReproductiveFunctions.crossover(parent1=parents[i], parent2=parents[i+1])

            child1 = ReproductiveFunctions.mutation(child1, MUTATION_RATE)
            child2 = ReproductiveFunctions.mutation(child2, MUTATION_RATE)

            self.population.append(child1)
            self.population.append(child2)


    def evaluate_population(self, selection: Selection):
        """
        This method will evaluate the existing population and kill the unfit chromosomes
        """
        # updating the fitness scores
        self.problem.population = self.population
        self.fitness_scores = self.problem.fitness_score()

        # Selecting the unfit chromosomes
        if selection == Selection.Random:
            survivors = SelectionFunctions.random(self.population, self.fitness_scores, POPULATION_SIZE)
        elif selection == Selection.Truncation:
            survivors = SelectionFunctions.truncation(self.population, self.fitness_scores, POPULATION_SIZE)
        elif selection == Selection.ProportionalSelection:
            survivors = SelectionFunctions.proportional_selection(self.population, self.fitness_scores, POPULATION_SIZE)
        elif selection == Selection.RankBasedSelection:
            survivors = SelectionFunctions.rank_based_selection(self.population, self.fitness_scores, POPULATION_SIZE)
        elif selection == Selection.BinaryTournament:
            survivors = SelectionFunctions.binary_tournament(self.population, self.fitness_scores, POPULATION_SIZE)

        # killing the unfit chromosomes
        self.population = survivors
        self.problem.population = self.population
        self.fitness_scores = self.problem.fitness_score()

        # incrementing the generation
        self.generation += 1

    
    def best_fitness_score(self):
        """
        This method will return the best fitness score of the current population
        """
        return max(self.fitness_scores)

    
    def worst_fitness_score(self):
        """
        This method will return the worst fitness score of the current population
        """
        return min(self.fitness_scores)
