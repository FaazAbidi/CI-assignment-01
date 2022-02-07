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
        This method will perform crossover on the parents and return the child. It selects a random range and selects a sublist from the parents
        and merges them.
        We have eliminated the possibility of wrong chromosomes. 
        """
        crossover_point1 = random.randint(0, len(parent1)-1)
        crossover_point2 = random.randint(crossover_point1, len(parent1)-1)

        child = parent1[crossover_point1:crossover_point2]
        from_parent_2a = parent2[0:crossover_point1]
        from_parent_2b = parent2[crossover_point2:len(parent2)]

        for i in range(len(from_parent_2b)):
            if from_parent_2b[i] in child:
                from_parent_2b[i] = parent1[crossover_point2+i]
        for i in range(len(from_parent_2a)-1,-1,-1):
            if from_parent_2a[i] in child and from_parent_2a[i] not in from_parent_2b:
                from_parent_2a[i] = parent1[i-crossover_point1]
        
        child = from_parent_2a + child + from_parent_2b

        for i in range(len(child)):
            if child.count(child[i]) > 1:
                if parent1[i] not in child:
                    child[i] = parent1[i]
                elif parent2[i] not in child:
                    child[i] = parent2[i]
                else:
                    child[i] = [x for x in parent1 if x not in child][0]
        
        # check if the child is valid
        for each in child:
            assert child.count(each) == 1
    
        return child



    @staticmethod
    def mutation(child: list, mutation_rate: float()) -> list:
        """
        For the mutation, we will swap two values in the child at mutation_rate probability
        """
        random_val = random.random()
        if random_val < mutation_rate:
            index1 = random.randint(0, len(child)-1)
            index2 = random.randint(0, len(child)-1)
            child[index1], child[index2] = child[index2], child[index1]
        
        return child