from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GraphColoringProblem

# instantiate the TSP problem
TSP = TSPProblem()
# applying the EA to the TSP problem
EA = EA(TSP)

print(TSP.crossover(parent1=[1,3,4,5,6],parent2=[6,5,3,5,7]))

tsp = TSPProblem()
kp = KnapsackProblem()
ea = EA(kp)


# print(kp.data)


# # print(len(ea.population))
# # print(ea.population)
# print(SelectionFunctions.binary_tournament([1,2,3,4,5,6,7,8,9,10], [10,15,20,30,25,5,6,7,90,1000], 3,fit_bias=False))

# print(ReproductiveFunctions.crossover(parent1=[1,2,7,3,4,5,8,9,6,10], parent2=[10,6,8,9,7,3,4,1,5,2]))
# for u in range(10000):
# print(SelectionFunctions.proportional_selection(
#     [1,2,3,4,5,6,7,8,9,10],
#     [300,4,5,6,1,2,8,9,10,7],
#     5,
#     True
# ))
