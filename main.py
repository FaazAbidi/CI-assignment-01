from EA import *
from Problems.tsp_problem import TSPProblem
from Problems.knapsack_problem import KnapsackProblem
from Problems.graph_coloring_problem import GraphColoringProblem

# instantiate the TSP problem
TSP = TSPProblem()
# applying the EA to the TSP problem
EA = EA(TSP)

print(TSP.crossover(parent1=[1,3,4,5,6],parent2=[6,5,3,5,7]))

# for i in range(GENERATIONS):
#     print(EA.generation, EA.worst_fitness_score(), len(EA.population))
#     EA.generate_offspring(Selection.ProportionalSelection)
#     EA.evaluate_population(Selection.Truncation)


# for u in range(10000):
# print(SelectionFunctions.proportional_selection(
#     [1,2,3,4,5,6,7,8,9,10],
#     [300,4,5,6,1,2,8,9,10,7],
#     5,
#     True
# ))