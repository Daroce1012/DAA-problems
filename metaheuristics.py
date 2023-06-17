

import numpy as np
import random

#CREAR LA POBLACION
def initialize_population(pop_size):
    population_set = []

    # print(pop_size)
    
    for i in range(len(pop_size)):
        print(pop_size[i])
        sol_i = pop_size[i] 
        population_set.append(sol_i)
        
    return population_set


def valid_solution(solution):
    dicc = {}
    for p in solution:
        for day in p:
            if day in dicc:
                return False
            dicc[day] = p
    return True

#EVALUACION
def fitness_eval(x):

    if valid_solution(x):
        return 1
    
    return 0

def get_all_fitnes(population_set, pop_size):
    fitnes_list = np.zeros(len(population_set), dtype=int)

    print("FITNES LIST")
    print(fitnes_list)

    print("POP SIZE")
    print(pop_size)

    #Looping over all solutions computing the fitness for each solution
    for i in range(len(population_set)):
        fitnes_list[i] = fitness_eval(population_set[i])

    return fitnes_list

#SELECCION
def progenitor_selection(population_set,fitnes_list):

    progenitor_list_a = [] 
    progenitor_list_b = [] 

    list_change=True

    for i in range(len(fitnes_list)):
        if list_change:
            progenitor_list_a.append(population_set[i])
            list_change = False
        else:
            progenitor_list_b.append(population_set[i])
            list_change = True
    
    
    return np.array([progenitor_list_a,progenitor_list_b])

#VARIACION
def mate_progenitors(prog_a, prog_b):

    print("prog_a")
    print(prog_a)

    print("prog_b")
    print(prog_b)

    half = (int)(len(prog_a)/2)

    print("HALF")
    print(half)

    new_solution = []

    for i in range(half):
        new_solution.append(prog_a[i])
    for i in range(half, len(prog_b)):
        new_solution.append(prog_b[i])

    if valid_solution(new_solution):
        return new_solution

    return []
#CASO EN EL QUE LA SOLUCION NO ES VALIDAA
    
def mate_population(progenitor_list):

    new_population_set = []

    # list_a = [[[96, 64, 87], [69, 65], [12, 58, 61], [71, 88, 42, 98], [67, 51]], [[76, 19, 65, 40], [55, 56], [74, 3], [96, 68, 27], [69, 31, 64]]]

    # list_b = [[[94, 53], [41, 28], [49, 16], [87, 66, 96], [38, 36, 51]]]

    # progenitor_list = np.array([list_a,list_b])

    print("PROGENITOR_LIST")
    print(progenitor_list)

    if len(progenitor_list[0]) == 0:
        return new_population_set
    if len(progenitor_list[1]) == 0:
        return progenitor_list[0]

    # print(min(len(progenitor_list[0]), len(progenitor_list[1])))

    pos = 0

    for i in range(min(len(progenitor_list[0]), len(progenitor_list[1]))):
        # if i < len(progenitor_list[0]) and i < len(progenitor_list[1]):
        prog_a, prog_b = progenitor_list[0][i], progenitor_list[1][i]
        offspring = mate_progenitors(prog_a, prog_b)
        if not len(offspring) == 0:
            new_population_set.append(offspring)
        pos = i + 1

    if pos < len(progenitor_list[0]):
        for i in range(pos, len(progenitor_list[0])):
            new_population_set.append(progenitor_list[0][i])
    if pos < len(progenitor_list[1]):
        for i in range(pos, len(progenitor_list[1])):
            new_population_set.append(progenitor_list[1][i])
        
    return new_population_set

def mutate_offspring(offspring, mutation_rate):
    #TODO: Your code here!
    return None
    
def mutate_population(new_population_set, mutation_rate):
    mutated_pop = []
    for offspring in new_population_set:
        mutated_pop.append(mutate_offspring(offspring, mutation_rate))
    return np.array(mutated_pop)

def stop_criterion(t):
    # return t >= 10000 
    return t >=50


# def evolutionary_algorithm(pop_size, mutation_rate = 0.3):  
def evolutionary_algorithm(pop_size):
    populations = []
    best_solution = [-1,np.inf,np.array([])] #[iteration, fitness, solution]
    
    populations.append(initialize_population(pop_size))
    t = 0
    
    while not stop_criterion(t):
        fitnes_list = get_all_fitnes(populations[t], pop_size)
        if t%100==0: print(t,  "fitness_mean: ", fitnes_list.mean(), "best_solution: ", best_solution)
            
        #Saving the best solution
        if fitnes_list.min() < best_solution[1]:
            best_solution[0] = t
            best_solution[1] = fitnes_list.min()
            best_solution[2] = np.array(populations[t])[fitnes_list.min() == fitnes_list]
    
        progenitor_list = progenitor_selection(populations[t],fitnes_list)
        new_population_set = mate_population(progenitor_list)
        # mutated_pop = mutate_population(new_population_set, mutation_rate)
        t = t+1
        if len(new_population_set) == 1 and valid_solution(new_population_set[0]):
            return new_population_set[0]

        if not len(new_population_set) == 0:
            populations.append(new_population_set)
        else:
            break
        
        # populations.append(mutated_pop)
    
    return best_solution

# evolutionary_algorithm()

def random_generator(courses = 5, solutions_count = 5):

    count = 0
    poblacion_set = []

    while count < solutions_count:

        solution = []

        for _ in range(courses):
            subjects = []
            count_subjects = random.randrange(2,5)
            for _ in range(count_subjects):
                subjects.append(random.randrange(1,100))
            subjects.sort()
            solution.append(subjects)

        print("solution")
        print(solution)

        poblacion_set.append(solution)
        count = count+1

    print("poblacion_set")
    print(poblacion_set)
    
    return poblacion_set



def main():
    
    print("Solucion")
    print(evolutionary_algorithm(random_generator()))
    # return evolutionary_algorithm(random_generator())

main()
