import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0, 5, 50)
y = np.cos(x)

plt.plot(x,y)

# Create a sine wave using NumPy and plot it using Matplotlib:

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.show()

# Generate random data points and fit a linear regression line:

x = np.linspace(0, 10, 50)
simple_function = 2 * x + 1

y = simple_function + np.random.randn(50)

plt.scatter(x, y, label='Data Points')
plt.plot(x, simple_function, color='red', label='Linear Regression Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Regression')
plt.legend()
plt.show()

from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

Z = np.cos(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title('3D Surface Plot')
plt.show()


# Generate a histogram with a normal distribution:
data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=20, color='blue', edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram with Normal Distribution')
plt.show()

# Create a scatter plot with points colored based on their distance from the origin:

x = np.random.randn(100)
y = np.random.randn(100)
distances = np.sqrt(x**2 + y**2)

plt.scatter(x, y, c=distances, cmap='viridis', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Distance Color Map')
plt.colorbar(label='Distance from Origin')
plt.show()

# Combine multiple subplots:

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y1, label='Sin(x)', color='blue')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, y2, label='Cos(x)', color='green')
plt.legend()

plt.tight_layout()
plt.show()


# Create a bar chart with error bars:


categories = ['A', 'B', 'C']
values = [5, 7, 3]
errors = [0.5, 1, 0.2]

plt.bar(categories, values, yerr=errors, color='orange', edgecolor='black')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart with Error Bars')
plt.show()


# Generate a heatmap for a 2D array with annotation:

data = np.random.rand(5, 5)
plt.imshow(data, cmap='viridis', interpolation='nearest')

for i in range(5):
    for j in range(5):
        plt.text(j, i, f'{data[i, j]:.2f}', ha='center', va='center', color='white')

plt.colorbar()
plt.title('Heatmap with Annotation')
plt.show()

# Plot a quiver plot with random vectors:

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
u = np.cos(x)
v = np.sin(2*x)

plt.quiver(x, y, u, v, scale=5, color='green', width=0.007)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Quiver Plot')
plt.show()

# Create a pie chart with labels and explode a slice:

labels = ['Category A', 'Category B', 'Category C']
sizes = [30, 45, 25]
explode = (0, 0.1, 0)

plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Pie Chart with Exploded Slice')
plt.show()

# Generate a scatter plot with a regression line:

x = np.linspace(0, 10, 50)
y = 2 * x + 1 + np.random.randn(50)

plt.scatter(x, y, label='Data Points')
coefficients = np.polyfit(x, y, 1)
regression_line = np.polyval(coefficients, x)
plt.plot(x, regression_line, color='red', label='Regression Line')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Regression Line')
plt.legend()
plt.show()

# Create a box plot with multiple datasets:

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(3, 1, 100)
data3 = np.random.normal(-2, 2, 100)

plt.boxplot([data1, data2, data3], labels=['Set 1', 'Set 2', 'Set 3'])
plt.xlabel('Data Sets')
plt.ylabel('Values')
plt.title('Box Plot with Multiple Datasets')
plt.show()

# Plot a stacked area chart:

x = np.linspace(0, 5, 100)
y1 = x**2
y2 = x**3

plt.stackplot(x, y1, y2, labels=['x^2', 'x^3'], colors=['blue', 'green'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Stacked Area Chart')
plt.legend()
plt.show()

# Create a radar chart for multiple categories with randomly generated data:

categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = np.random.randint(1, 10, 5)

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
values += values[:1]
angles += angles[:1]

plt.polar(angles, values, marker='o', linestyle='-', color='orange', linewidth=2)
plt.fill(angles, values, color='orange', alpha=0.25)
plt.title('Radar Chart')
plt.show()


# Combine line and bar plots with dual y-axes:

x = np.linspace(0, 5, 50)
y1 = x**2
y2 = 10 * np.exp(-x)

fig, ax1 = plt.subplots()

ax1.plot(x, y1, color='blue', label='x^2')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('y1', color='blue')
ax1.tick_params('y', colors='blue')

ax2 = ax1.twinx()
ax2.bar(x, y2, alpha=0.3, color='green', label='10 * exp(-x)')
ax2.set_ylabel('y2', color='green')
ax2.tick_params('y', colors='green')

fig.tight_layout()
plt.title('Dual Axes Plot')
plt.show()



def mandelbrot( h,w, maxit=20 ):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    
    for i in range(maxit):
       z = z**2 + c
       diverge = z*np.conj(z) > 2**2 # who is diverging
       div_now = diverge & (divtime==maxit) # who is diverging now
       divtime[div_now] = i # note when
       z[diverge] = 2 # avoid diverging too much
    
    return divtime
plt.imshow(mandelbrot(400,400))
plt.show()