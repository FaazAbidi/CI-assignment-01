from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GC
from Problems.problem import Problem
import numpy as np

from test import check_chromosome

# instantiate the TSP problem
# TSP = TSPProblem()
gc = GC()
# applying the EA to the TSP problem
# EA = EA(TSP)
EA = EA(gc)
# print(EA.population)
# print(gc.crossover(parent1=[(0,0,0), (1,1,1), (5,5,5), (7,7,7)],parent2=[(3,3,3), (4,4,4), (5,5,5), (1,1,1)]))
# plt.rcParams['text.usetex'] = True
# plt.rcParams["figure.figsize"] = (10,8)


# instantiate the TSP problem
# TSP = TSPProblem()
# # # applying the EA to the TSP problem
# EA = EA(TSP)

best_fitness_scores = []
averaga_fitness_scores = []

for i in range(GENERATIONS):
# #     # print(EA.population)
    print(i)
    EA.generate_offspring(Selection.BinaryTournament)
    EA.evaluate_population(Selection.Truncation)
    best_fitness_scores.append(EA.best_fitness_score())
    averaga_fitness_scores.append(EA.averaga_fitness_score())
# g = EA.population
# for i in g:
#     print(i)
print(best_fitness_scores)
print(averaga_fitness_scores)
# g = EA.population
# for i in g:
#     print(i)
# plt.plot(best_fitness_scores, label='Best Fitness Score')
# plt.plot(averaga_fitness_scores, label='Average Fitness Score')
# plt.annotate("Best So Far: {}".format(best_fitness_scores[-1]), # this is the text
#                  (GENERATIONS,best_fitness_scores[-1]), # these are the coordinates to position the label
#                  textcoords="offset points", # how to position the text
#                  xytext=(0,10), # distance from text to points (x,y)
#                  ha='center') 
# plt.title(r'BT & Truncation')
# plt.xlabel(r'Generations')
# plt.ylabel(r'Fitness Score')
# plt.legend()
# plt.show()

# for i in range(GENERATIONS):
#     print(EA.generation, EA.best_fitness_score(), len(EA.population))
#     EA.generate_offspring(Selection.ProportionalSelection)
#     EA.evaluate_population(Selection.Truncation)

# for u in range(10000):
# print(SelectionFunctions.proportional_selection(
#     [1,2,3,4,5,6,7,8,9,10],
#     [300,4,5,6,1,2,8,9,10,7],
#     5,
#     True
# ))

