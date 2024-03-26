import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.normal(loc=0, scale=1, size=1000)

# Create histogram with custom bin colors
plt.hist(data, bins=20, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram with Custom Bin Colors')
plt.show()

color_list = []
fig, ax = plt.subplots()

N, bins, patches = ax.hist(data, edgecolor='white', bins = 20, linewidth=1)

for i in range(0,3):
    patches[i].set_facecolor('b')
for i in range(3,5):    
    patches[i].set_facecolor('r')
for i in range(5, len(patches)):
    patches[i].set_facecolor('black')

plt.show()






