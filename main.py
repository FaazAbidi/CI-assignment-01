from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GraphColoringProblem
from reproductive_functions import *



tsp = TSPProblem()
ea = EA(tsp)

ea.generate_offspring()


# print(SelectionFunctions.binary_tournament([1,2,3,4,5], [10,15,20,30,25]))

print(ReproductiveFunctions.crossover(parent1=[1,2,3,4,5], parent2=[3,4,1,5,2]))