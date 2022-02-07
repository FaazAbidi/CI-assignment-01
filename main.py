from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GraphColoringProblem
from reproductive_functions import *



tsp = TSPProblem()
ea = EA(tsp)

while ea.generation < GENERATIONS:
    print(ea.generation, ea.worst_fitness_score())
    ea.generate_offspring(Selection.ProportionalSelection)
    ea.evaluate_population(Selection.Truncation)


# # print(len(ea.population))
# # print(ea.population)
# print(SelectionFunctions.binary_tournament([1,2,3,4,5,6,7,8,9,10], [10,15,20,30,25,5,6,7,90,1000], 3,fit_bias=False))

# print(ReproductiveFunctions.crossover(parent1=[1,2,7,3,4,5,8,9,6,10], parent2=[10,6,8,9,7,3,4,1,5,2]))