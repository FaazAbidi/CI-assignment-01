from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GraphColoringProblem
from Problems.graph_coloring_problem import GC
from Problems.problem import Problem
import numpy as np
from matplotlib import pyplot as plt
<<<<<<< HEAD
=======
from tqdm import tqdm


plt.rcParams['text.usetex'] = True
plt.rcParams["figure.figsize"] = (10,8)

>>>>>>> e6ef9063f95291b59bba5210445d929b6da807f1

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

file = open("Results/TSP/results_BT_and_Truncation.txt", "w")

for i in range(GENERATIONS):
    file.write("{},{},{}\n".format(EA.generation, abs(EA.best_fitness_score()), abs(EA.averaga_fitness_score())))
    print(EA.generation, abs(EA.best_fitness_score()), len(EA.population))
    EA.generate_offspring(Selection.BinaryTournament)
    EA.evaluate_population(Selection.Truncation)
    best_fitness_scores.append(abs(EA.best_fitness_score()))
    averaga_fitness_scores.append(abs(EA.averaga_fitness_score()))

print("Best canditate: ", EA.population[EA.fitness_scores.index(EA.best_fitness_score())])

# # plotting the results
plt.plot(best_fitness_scores, label='Best Fitness Score',)
plt.plot(averaga_fitness_scores, label='Average Fitness Score',)
plt.annotate("{}".format(round(best_fitness_scores[-1],3)),
                 (len(best_fitness_scores)-1,best_fitness_scores[-1]), 
                 textcoords="offset points",
                 xytext=(0,10), 
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='green')
                 )
plt.annotate("{}".format(round(averaga_fitness_scores[-1],3)),
                 (len(averaga_fitness_scores)-1,averaga_fitness_scores[-1]), 
                 textcoords="offset points",
                 xytext=(0,-20), 
                 ha='center',
                 arrowprops=dict(arrowstyle="->", color='green')
                 )
plt.title(r'BT \& Truncation')
plt.xlabel(r'Generations')
plt.ylabel(r'Fitness Score')
plt.legend()
plt.show()

