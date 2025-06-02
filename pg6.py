import numpy as np


class PSO:
    def __init__(self, dim, bounds, func, c1=0.8, c2=0.4, particles=20, iters=100):
        self.dim, self.bounds, self.func = dim, bounds, func
        self.c1, self.c2, self.particles, self.iters = c1, c2, particles, iters


    def optimize(self):
        loc = np.random.uniform(self.bounds[:, 0], self.bounds[:, 1], (self.particles, self.dim))
        vel = pbest = loc.copy()
        fit = self.func(loc)
        gbest = loc[np.argmin(fit)]
        best_cost = np.min(fit)  # Track the best cost


        for i in range(self.iters):
            r = np.random.rand(self.particles, 2)
            vel = 0.9 * vel + self.c1 * r[:, 0:1] * (pbest - loc) + self.c2 * r[:, 1:2] * (gbest - loc)
            loc = np.clip(loc + vel, self.bounds[:, 0], self.bounds[:, 1])
            fit_new = self.func(loc)
            pbest[fit_new < fit], fit = loc[fit_new < fit], np.minimum(fit, fit_new)
            gbest = loc[np.argmin(fit)] if np.min(fit) < self.func(gbest) else gbest
            best_cost = np.min(fit)


        return gbest, self.func(gbest), best_cost


# Function and bounds
def f(x): return x**2 + 5*x + 20  # x is already a 1D array
bounds = np.array([[-10, 10]])


# PSO optimization
pso = PSO(1, bounds, f, particles=9, iters=50)
best_solution, best_value, best_cost = pso.optimize()
print(f"Best Solution: {best_solution}, Function Value: {best_value}, Cost: {best_cost}")




