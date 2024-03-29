from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GC
from Problems.problem import Problem
import numpy as np
from matplotlib import pyplot as plt    

# instantiate the TSP problem
# TSP = TSPProblem()
# applying the EA to the TSP problem
# EA = EA(TSP)

# print(TSP.crossover(parent1=[1,3,4,5,6],parent2=[6,5,3,5,7]))

tsp = TSPProblem()
kp = KnapsackProblem()
ea = EA(kp)


# print(kp.data)


# print(len(ea.population))
# print(ea.population)
# print(SelectionFunctions.binary_tournament([1,2,3,4,5,6,7,8,9,10], [10,15,20,30,25,5,6,7,90,1000], 3))
while ea.generation < GENERATIONS:
    print(ea.generation, ea.worst_fitness_score())
    ea.generate_offspring(Selection.ProportionalSelection)
    ea.evaluate_population(Selection.Truncation)

# print(ReproductiveFunctions.crossover(parent1=[1,2,7,3,4,5,8,9,6,10], parent2=[10,6,8,9,7,3,4,1,5,2]))
# for u in range(10000):
# print(SelectionFunctions.proportional_selection(
#     [1,2,3,4,5,6,7,8,9,10],
#     [300,4,5,6,1,2,8,9,10,7],
#     5,
#     True
# ))

plt.rcParams['text.usetex'] = True
plt.rcParams["figure.figsize"] = (10,8)



def main():
    # instantiate a problem
    # TSP = TSPProblem()
    gc = GC()
    # # applying the EA to the problem
    ea = EA(gc)
    best_fitness_scores = []
    averaga_fitness_scores = []

    # file = open("Results/TSP/results_BT_and_Truncation.txt", "w")

    for i in range(GENERATIONS):
        # file.write("{},{},{}\n".format(ea.generation, abs(ea.best_fitness_score()), abs(ea.averaga_fitness_score())))
        print(ea.generation, abs(ea.best_fitness_score()), len(ea.population))

        # evolutionary process
        ea.generate_offspring(Selection.RankBasedSelection)
        ea.evaluate_population(Selection.RankBasedSelection)

        # append the best fitness score to the list for plotting
        best_fitness_scores.append(abs(ea.best_fitness_score()))
        averaga_fitness_scores.append(abs(ea.averaga_fitness_score()))

    print("Fittest canditate: ", ea.population[ea.fitness_scores.index(ea.best_fitness_score())])

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
    plt.title(r'Truncation and Truncation')
    plt.xlabel(r'Generations')
    plt.ylabel(r'Fitness Score')
    plt.legend()
    plt.show()


main()
