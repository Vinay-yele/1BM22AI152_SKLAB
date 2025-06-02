import numpy as np

# Parameters
num_ants, num_iter, rho, Q = 2, 5, 100, 5  # Number of ants, iterations, evaporation rate, pheromone factor

dist = np.array([[0,10,17,10], [10,0,10,10], [17,10,0,10], [10,10,10,0]])  # Distance matrix
n = len(dist)  # Number of cities
pher = np.ones((n, n))  # Initialize pheromone matrix with ones

# Function to calculate the cost (total distance) of a given path
def cost(path):
    return sum(dist[path[i], path[i+1]] for i in range(n-1)) + dist[path[-1], path[0]]

# Function to update pheromone levels based on solutions
def update(pher, sols):
    for path in sols:
        for i in range(n):
            pher[path[i], path[(i+1) % n]] += Q / cost(path)  # Pheromone deposit
    pher *= (1 - rho)  # Evaporation of pheromone

# Ant Colony Optimization function
def aco():
    best_path, best_cost = None, float('inf')
    for _ in range(num_iter):
        sols = [np.random.permutation(n) for _ in range(num_ants)]  # Generate solutions
        update(pher, sols)  # Update pheromones
        for path in sols:
            c = cost(path)
            if c < best_cost:
                best_path, best_cost = path, c  # Update best solution
    return best_path, best_cost

# Run the ACO algorithm and print the best solution
print("Best solution:", *aco())
