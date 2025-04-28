import random

def create_initial_population(size, num_cities):
    population = []
    for _ in range(size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

def fitness(individual, distance_matrix):
    return 1 / calculate_distance(individual, distance_matrix)

def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probs = [f/total_fitness for f in fitnesses]
    return population[random.choices(range(len(population)), probs)[0]]

def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[start:end+1] = parent1[start:end+1]

    ptr = 0
    for gene in parent2:
        if gene not in child:
            while child[ptr] != -1:
                ptr += 1
            child[ptr] = gene
    return child

def mutate(individual):
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]

def genetic_algorithm_tsp(distance_matrix, pop_size=100, generations=500, mutation_rate=0.01):
    num_cities = len(distance_matrix)
    population = create_initial_population(pop_size, num_cities)

    for _ in range(generations):
        fitnesses = [fitness(individual, distance_matrix) for individual in population]
        new_population = []

        for _ in range(pop_size):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)

            if random.random() < mutation_rate:
                mutate(child)
            new_population.append(child)

        population = new_population

    best_individual = max(population, key=lambda ind: fitness(ind, distance_matrix))
    best_distance = calculate_distance(best_individual, distance_matrix)
    return best_individual, best_distance

# Ví dụ sử dụng
path, distance = genetic_algorithm_tsp(distance_matrix)
print("Đường đi ngắn nhất (Genetic Algorithm):", path)
print("Chi phí:", distance)