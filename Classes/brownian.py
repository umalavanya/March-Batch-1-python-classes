import random
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, initial_position=0):
        self.position = initial_position

    def move(self):
        # Generate a random displacement (step) for the particle
        step = random.choice([-1, 1])
        # Update the position of the particle
        self.position += step

    def get_position(self):
        return self.position

class BrownianMotionSimulation:
    def __init__(self, num_particles, num_steps):
        self.num_particles = num_particles
        self.num_steps = num_steps
        self.particles = [Particle() for _ in range(num_particles)]

    def simulate(self):
        for _ in range(self.num_steps):
            for particle in self.particles:
                particle.move()

    def get_positions_at_time(self, time):
        # Simulate until the specified time
        for _ in range(time):
            for particle in self.particles:
                particle.move()
        # Return positions of all particles at the specified time
        return [particle.get_position() for particle in self.particles]

# Parameters for the simulation
num_particles = 1000  # Number of particles
num_steps = 10  # Number of time steps
time = 10  # Time at which to observe the position distribution

# Create a Brownian motion simulation object
simulation = BrownianMotionSimulation(num_particles, num_steps)

# Run the simulation
positions_at_time_T = simulation.get_positions_at_time(time)

# Plot position distribution
plt.hist(positions_at_time_T, bins=30, density=True, color='skyblue', edgecolor='black')
plt.title(f'Position Distribution at Time T = {time}')
plt.xlabel('Position')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
