import numpy as np
import matplotlib.pyplot as plt

# --- Fitness Function ---
def fitness_function(x):
    return x * np.sin(x)

# --- Genetic Algorithm Parameters ---
population_size = 20
generations = 50
crossover_rate = 0.8
mutation_rate = 0.1
gene_bounds = (0, 10)  # valid range of x values

# --- Initialize Population (array of real numbers) ---
population = np.random.uniform(gene_bounds[0], gene_bounds[1], size=population_size)

# --- Track Best Fitness Over Generations ---
best_fitness_history = []

# --- Genetic Algorithm Main Loop ---
for generation in range(generations):
    # Step 1: Evaluate Fitness
    fitness = fitness_function(population)

    # Step 2: Selection (Select top 50%)
    sorted_indices = np.argsort(fitness)[::-1]
    top_half = population[sorted_indices[:population_size // 2]]

    # Step 3: Crossover
    children = []
    while len(children) < population_size:
        if np.random.rand() < crossover_rate:
            parent1, parent2 = np.random.choice(top_half, 2, replace=False)
            child = (parent1 + parent2) / 2
        else:
            child = np.random.choice(top_half)
        # Step 4: Mutation
        if np.random.rand() < mutation_rate:
            child += np.random.uniform(-1.0, 1.0)
        # Keep child within bounds
        child = np.clip(child, gene_bounds[0], gene_bounds[1])
        children.append(child)

    # Step 5: Replace old population with new one
    population = np.array(children)

    # Track best fitness in current generation
    best_fitness = np.max(fitness_function(population))
    best_fitness_history.append(best_fitness)

    print(f"Generation {generation + 1}: Best Fitness = {best_fitness:.4f}")

# --- Final Result ---
best_solution = population[np.argmax(fitness_function(population))]
print(f"\n✅ Best Solution: x = {best_solution:.4f}, f(x) = {fitness_function(best_solution):.4f}")

# --- Plot Fitness Over Generations ---
plt.plot(best_fitness_history, label='Best Fitness')
plt.title("Fitness Over Generations")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.legend()
plt.grid(True)
plt.show()
