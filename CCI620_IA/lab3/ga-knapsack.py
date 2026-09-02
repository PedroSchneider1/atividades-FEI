from pyeasyga import pyeasyga
import matplotlib.pyplot as plt
import random
import copy
import numpy as np

# setup data
data = [{'name': 'green', 'value': 4, 'weight': 12},
        {'name': 'gray', 'value': 2, 'weight': 1},
        {'name': 'yellow', 'value': 10, 'weight': 4},
        {'name': 'orange', 'value': 1, 'weight': 1},
        {'name': 'blue', 'value': 2, 'weight': 2}]

tamanho_populacao = 20
geracoes = 50

ga = pyeasyga.GeneticAlgorithm(data,
                               population_size = tamanho_populacao,
                               generations = geracoes,
                               crossover_probability = 0.9,
                               mutation_probability = 0.3,
                               elitism = True,
                               maximise_fitness = True
                               )

def my_create_individual(data):
    individual = []
    for item in data:
        individual.append(random.randint(0, 15))
    return individual

ga.create_individual = my_create_individual

def aptidao(individual, data):
    value, weight = 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            value += item['value']
            weight += item['weight']
    if weight > 15:
        return 0
    return value

ga.fitness_function = aptidao

# def crossover(parent_1, parent_2):
#     crossover_index = random.randrange(1, len(parent_1))
#     child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
#     child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
#     return child_1, child_2

# ga.crossover_function = crossover

# def my_mutation(individual):
#     mutate_index = random.randrange(len(individual))
#     individual[mutate_index] = random.randint(0,15)

# ga.mutate_function = my_mutation

# def my_selection(population):
#     fitnesses = [individual[1] for individual in population]
#     total_fitness = sum(fitnesses)
#     probs = [fitness / total_fitness for fitness in fitnesses]    
#     return probs
# ga.selection_function = my_selection


ga.run()

print("best solution")
print(ga.best_individual())

print("last generation")
for individual in ga.last_generation():
    print(individual)
