import random
import numpy as np
random_population = []
for element in range(5):
            chromosome = []
            for i in range(28):
                print(i)
                flag = True
                while flag:
                    np.random.seed()
                    color = random.randint(0, 80)
                    gene = (color,color,color)                                  
                    if gene not in chromosome:
                        chromosome.append(gene)
                        print(gene)
                        flag = False
                    else:
                        continue
            random_population.append(chromosome)
            print(chromosome)