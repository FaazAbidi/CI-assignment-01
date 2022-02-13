from Problems.graph_coloring_problem import GC
from EA import EA

gc = GC()
ea = EA(gc)

print(ea.population)