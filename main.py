from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GraphColoringProblem
from matplotlib import pyplot as plt
# plt.rcParams['text.usetex'] = True
plt.rcParams["figure.figsize"] = (10,8)


# instantiate the TSP problem
TSP = TSPProblem()
# # applying the EA to the TSP problem
EA = EA(TSP)

best_fitness_scores = []
averaga_fitness_scores = []

for i in range(GENERATIONS):
    # print(EA.generation, EA.best_fitness_score(), len(EA.population))
    EA.generate_offspring(Selection.BinaryTournament)
    EA.evaluate_population(Selection.Truncation)
    best_fitness_scores.append(EA.best_fitness_score())
    averaga_fitness_scores.append(EA.averaga_fitness_score())


# # plotting the results
plt.plot(best_fitness_scores, label='Best Fitness Score')
plt.plot(averaga_fitness_scores, label='Average Fitness Score')
plt.annotate("Best So Far: {}".format(best_fitness_scores[-1]), # this is the text
                 (GENERATIONS,best_fitness_scores[-1]), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') 
plt.title(r'BT & Truncation')
plt.xlabel(r'Generations')
plt.ylabel(r'Fitness Score')
plt.legend()
plt.show()

