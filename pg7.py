import numpy as np

# Objective Function (Sphere Function)
def objective_function(x):
    return np.sum(x**2)

# Grey Wolf Optimizer
def grey_wolf_optimization(obj_func, dim, n_wolves, max_iter, bounds):
    # Initialize wolves' positions
    wolves = np.random.uniform(bounds[0], bounds[1], (n_wolves, dim))
    alpha, beta, delta = np.zeros(dim), np.zeros(dim), np.zeros(dim)
    alpha_score, beta_score, delta_score = float("inf"), float("inf"), float("inf")

    print("Initial Wolves' Positions:")
    print(wolves)

    for t in range(max_iter):
        for i in range(n_wolves):
            fitness = obj_func(wolves[i])
            # Update alpha, beta, and delta
            if fitness < alpha_score:
                delta_score, delta = beta_score, beta.copy()
                beta_score, beta = alpha_score, alpha.copy()
                alpha_score, alpha = fitness, wolves[i].copy()
            elif fitness < beta_score:
                delta_score, delta = beta_score, beta.copy()
                beta_score, beta = fitness, wolves[i].copy()
            elif fitness < delta_score:
                delta_score, delta = fitness, wolves[i].copy()

        a = 2 - t * (2 / max_iter)  # Linearly decreasing from 2 to 0

        for i in range(n_wolves):
            for j in range(dim):
                r1, r2 = np.random.rand(), np.random.rand()
                A1, C1 = 2*a*r1 - a, 2*r2
                D_alpha = abs(C1*alpha[j] - wolves[i][j])
                X1 = alpha[j] - A1*D_alpha

                r1, r2 = np.random.rand(), np.random.rand()
                A2, C2 = 2*a*r1 - a, 2*r2
                D_beta = abs(C2*beta[j] - wolves[i][j])
                X2 = beta[j] - A2*D_beta

                r1, r2 = np.random.rand(), np.random.rand()
                A3, C3 = 2*a*r1 - a, 2*r2
                D_delta = abs(C3*delta[j] - wolves[i][j])
                X3 = delta[j] - A3*D_delta

                wolves[i][j] = (X1 + X2 + X3) / 3

        print(f"\nIteration {t+1}/{max_iter}: Best Fitness = {alpha_score:.5f}")

    print("\nOptimization Complete!")
    print("Best Position Found (Alpha Wolf):", alpha)
    print("Best Fitness Value:", alpha_score)

# Parameters
dim = 5
n_wolves = 10
max_iter = 20
bounds = (-10, 10)

# Run GWO
grey_wolf_optimization(objective_function, dim, n_wolves, max_iter, bounds)
