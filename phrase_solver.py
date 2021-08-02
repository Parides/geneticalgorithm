# -*- coding: utf-8 -*-
# Use standard python package only.
import random 
import math
import numpy as np
import matplotlib as plt


POPULATION_SIZE = 50 # Change POPULATION_SIZE to obtain better fitness.

GENERATIONS = 100 # Change GENERATIONS to obtain better fitness.
SOLUTION_FOUND = False

CORSSOVER_RATE = 0.8 # Change CORSSOVER_RATE  to obtain better fitness.
MUTATION_RATE = 0.2 # Change MUTATION_RATE to obtain better fitness.

GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}''' #Available Genes

'''Change the solution below, to your liking. Make sure all of its characters are in the GENES variable. If not you can add them'''
SOLUTION = "Hello Varun :) How are you?" # Solution

"""
    POPULATION GENERATIONS
"""
def generate_population(size):
    
    population = []
    
    for i in range(size):
        individual = [random_gene() for i in range(len(SOLUTION))]
        population.append(individual)
    
    return population

def random_gene():
   return random.choice(GENES) 

def next_generation(previous_population):

    elite = sorted(previous_population, key = compute_fitness)

    elite_size = int(len(elite) * 0.1)
    next_generation = []
    next_generation.extend(elite[:10])

    for i in range(POPULATION_SIZE - elite_size):
        first_parent = selection(previous_population)
        second_parent = selection(previous_population)
    
        if i <= ((POPULATION_SIZE-elite_size) * CORSSOVER_RATE):
            offspring = crossover(first_parent, second_parent)
        else:
            offspring = mutation(random.choice(previous_population))

        next_generation.append(offspring)

    return next_generation   

"""
    FITNESS COMPUTATIONS
"""
def compute_fitness(individual):

    fitness = 0

    for indivdual_letter,solution_letter in zip(individual, SOLUTION):
        if indivdual_letter != solution_letter:
            fitness += 1
            
    return fitness

"""
    SORTING & PRINTING
"""
def sort_population(population):
    return sorted(population, key=compute_fitness, reverse = False) #lowest first
    
def printpop(population):
    return [print(f"{individual} -- {compute_fitness(individual)}") for  individual in population]


"""
    SELECTION METHODS
"""
def selection(population):

    first_pick = random.choice(population)
    second_pick = random.choice(population)

    first_pick_fitness = compute_fitness(first_pick)
    second_pick_fitness = compute_fitness(second_pick)

    '''The Battle'''
    if first_pick_fitness > second_pick_fitness:
        return second_pick
    else:
        return first_pick
    '''The Battle'''
    

"""
    OPERANDS
"""
def crossover(first_parent, second_parent):
    # UNIFORM CROSSOVER

    individual = []
    i = 0
    for first_parent_character, first_parent_character in zip(first_parent, second_parent):
        
        prob = random.random()

        if i % 2 == 0:
            individual.append(first_parent_character)
        if i % 2 != 0:
            individual.append(first_parent_character)
        
        i += 1
    return individual

def mutation(individual):
    
    individual_size = len(individual)

    draw = random.randint(0,individual_size-1)

    individual_characters = list(individual)    

    individual_characters[draw] = random_gene()

    mutated_individual = individual_characters
    
    return mutated_individual

def main(): 
    global POPULATION_SIZE 
    global GENERATIONS
    global SOLUTION_FOUND
    

    generation = 0

    population = generate_population(POPULATION_SIZE)
    
    
    while (True): # termination in code

        population_sorted = sorted(population, key = compute_fitness)

        if compute_fitness(population_sorted[0]) <= 0:
            jointed = ''.join(population_sorted[0])
            print("!!SOLUTION FOUND!!")
            print(f"Gen({generation}): {jointed} - Fitness : {compute_fitness(population_sorted[0])}")

            break
        else:
            generation += 1

        jointed = ''.join(population_sorted[0])
        print(f"Gen({generation}): {jointed} - Fitness : {compute_fitness(population_sorted[0])}")

        population = next_generation(population) 

if __name__ == '__main__': 
    main()