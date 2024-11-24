import numpy as np
import matplotlib.pyplot as plt

# Coefficients of the quadratic function
a = -8  # Change to positive for minimum, negative for maximum
b = 8
c = 8

# Create a function for the parabola
def parabola(x):
    return a * x**2 + b * x + c

# Calculate the vertex (x-coordinate)
vertex_x = -b / (2 * a)
vertex_y = parabola(vertex_x)

# Determine if it's a minimum or maximum
if a > 0:
    nature = "absolute minimum"
else:
    nature = "absolute maximum"

# Print vertex and nature
print(f"The vertex is at ({vertex_x}, {vertex_y}) and it is an {nature}.")

# Generate x values
x_values = np.linspace(vertex_x - 10, vertex_x + 10, 400)
y_values = parabola(x_values)

# Plot the parabola
plt.plot(x_values, y_values, label=f'Parabola: {a}x^2 + {b}x + {c}')
plt.scatter(vertex_x, vertex_y, color='red', zorder=5, label=f'Vertex ({vertex_x:.2f}, {vertex_y:.2f})')

# Labels and title
plt.title(f'Parabola with {nature}')
plt.xlabel('x')
plt.ylabel('f(x)')

# Show the vertex and the nature of the parabola
plt.axvline(x=vertex_x, linestyle='--', color='gray', label='Axis of Symmetry')
plt.axhline(y=vertex_y, linestyle='--', color='gray')
plt.legend()
plt.grid(True)


plt.show()
