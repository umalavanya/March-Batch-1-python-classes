import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the function representing the first-order ODE dy/dx = f(x, y)
def simple_function(x, y):
    return x + y

# Define the initial condition
y0 = 1.0

# Define the range of x values
x_range = (0, 10)

# Solve the ODE using scipy's solve_ivp function
solution = solve_ivp(simple_function, x_range, [y0], t_eval=np.linspace(x_range[0], x_range[1], 100))

# Plot the solution
plt.plot(solution.t, solution.y[0], label='Solution y(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of First-Order ODE: dy/dx = x + y')
plt.legend()
plt.grid(True)
plt.show()
