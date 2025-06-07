import numpy as np

# -------------------------------
# Parameters
# -------------------------------
a = 1.5
b = 2.3
dX = 3
dY = 25

L = 50          # Size of the domain
N = 50         # Number of points in X
dx = L / N
dy = dx
dt = 0.01       # Time step
T = 5          # Total Time
steps = round(T / dt)

# -------------------------------
# Initial conditions
# -------------------------------
x = np.zeros((N+2, N+2))
y = np.zeros((N+2, N+2))

# Random initial condition
#x[1:N+1, 1:N+1] = np.random.rand(N, N)
#y[1:N+1, 1:N+1] = np.random.rand(N, N)

# Small perturbation from the equilibrium initial condition
x[1:N+1, 1:N+1] = a*np.ones((N,N))+0.01*np.random.rand(N,N)
y[1:N+1, 1:N+1] = (b/a)*np.ones((N,N))+0.01*np.random.rand(N,N)

# -------------------------------
# Function to impose periodic conditions
# -------------------------------
def periodic_conditions(x, y):
    x[:, 0] = x[:, N]
    y[:, 0] = y[:, N]
    x[:, N+1] = x[:, 1]
    y[:, N+1] = y[:, 1]

    x[0, :] = x[N, :]
    y[0, :] = y[N, :]
    x[N+1, :] = x[1, :]
    y[N+1, :] = y[1, :]

# Imposing periodic conditions
periodic_conditions(x, y)

# -------------------------------
# Preparing the files
# -------------------------------
file_x = open("evolution_x.txt", "w")
file_y = open("evolution_y.txt", "w")

# -------------------------------
# Time simulation
# -------------------------------
dxdt = np.zeros((N+2, N+2))
dydt = np.zeros((N+2, N+2))
lap_x = np.zeros((N+2, N+2))
lap_y = np.zeros((N+2, N+2))

for step in range(steps):
    # Calculating the Laplacian and the derivatives
    for i in range(1, N+1):
        for j in range(1, N+1):
            lap_x[i, j] = (x[i+1, j] + x[i-1, j] + x[i, j+1] + x[i, j-1] - 4 * x[i, j]) / dx**2
            lap_y[i, j] = (y[i+1, j] + y[i-1, j] + y[i, j+1] + y[i, j-1] - 4 * y[i, j]) / dy**2

            dxdt[i, j] = a - (b + 1) * x[i, j] + x[i, j]**2 * y[i, j] + dX * lap_x[i, j]
            dydt[i, j] = b * x[i, j] - x[i, j]**2 * y[i, j] + dY * lap_y[i, j]

    # Updating variables
    x += dt * dxdt
    y += dt * dydt

    # Again, we impose the periodic conditions
    periodic_conditions(x, y)

    # Save in file
    for i in range(1, N+1):
        fila_x = ", ".join(f"{x[i, j]:.6f}" for j in range(2, N+2))
        fila_y = ", ".join(f"{y[i, j]:.6f}" for j in range(2, N+2))

        file_x.write(fila_x + "\n")
        file_y.write(fila_y + "\n")

    # To sepparate the data in temporal blocks
    file_x.write("\n")
    file_y.write("\n")

# -------------------------------
# To close the files
# -------------------------------
file_x.close()
file_y.close()

print("Evolution saved in 'evolution_x.txt' y 'evolution_y.txt'")
