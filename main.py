from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GC
from Problems.problem import Problem
import numpy as np

# instantiate the TSP problem
# TSP = TSPProblem()
gc = GC()
# applying the EA to the TSP problem
# EA = EA(TSP)
EA = EA(gc)

# print(gc.crossover(parent1=[(0,0,0), (1,1,1), (5,5,5), (7,7,7)],parent2=[(3,3,3), (4,4,4), (5,5,5), (1,1,1)]))



for i in range(GENERATIONS):
    print(EA.generation, EA.best_fitness_score(), len(EA.population))
    EA.generate_offspring(Selection.ProportionalSelection)
    EA.evaluate_population(Selection.Truncation)

# for u in range(10000):
# print(SelectionFunctions.proportional_selection(
#     [1,2,3,4,5,6,7,8,9,10],
#     [300,4,5,6,1,2,8,9,10,7],
#     5,
#     True
# ))