from enum import Enum
from EA import *
import random

class ReproductiveFunctions:
    """
    This class contains static methods of different reproduction functions like crossover and mutations
    """
    
    @staticmethod
    def crossover(parent1: list, parent2: list) -> list:
        """
        This method will perform crossover on the parents and return the child
        """
        crossover_point1 = random.randint(0, len(parent1)-1)
        crossover_point2 = random.randint(crossover_point1, len(parent2)-1)

        print(parent1, parent2)
        print(crossover_point1, crossover_point2)
        child = parent1[crossover_point1:crossover_point2]
        from_parent_2a = parent2[0:crossover_point1]
        from_parent_2b = parent2[crossover_point2:len(parent2)]

        print(from_parent_2a, child ,from_parent_2b)

        for i in range(len(from_parent_2b)):
            if from_parent_2b[i] not in child:
                child.append(from_parent_2b[i])
            else:
                child.append(parent1[i+crossover_point2])

        for i in range(len(from_parent_2a)-1,-1,-1):
            if from_parent_2a[i] not in child:
                child.insert(0,from_parent_2a[i])
            else:
                child.append(parent1[crossover_point1-i-1])

        return child



    @staticmethod
    def mutation():
        pass