import numpy as np
import matplotlib.pyplot as plt

# Define a utility function (you can change this to suit your scenario)
def utility(x, y):
    return x**0.5 + y**0.5

# Create a grid of x and y values
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)

# Create the plots
plt.figure(figsize=(12, 10))

# Scenario 1: Both products are good
Z1 = utility(X, Y)
plt.subplot(2, 2, 1)
plt.contourf(X, Y, Z1, levels=20, cmap='coolwarm')
plt.title('Both Products are Good')
plt.xlabel('Product X')
plt.ylabel('Product Y')

# Scenario 2: Both products are bad
Z2 = -utility(X, Y)
plt.subplot(2, 2, 2)
plt.contourf(X, Y, Z2, levels=20, cmap='coolwarm')
plt.title('Both Products are Bad')
plt.xlabel('Product X')
plt.ylabel('Product Y')

# Scenario 3: Product Y is good, Product X is bad
Z3 = utility(X, -Y)
plt.subplot(2, 2, 3)
plt.contourf(X, Y, Z3, levels=20, cmap='coolwarm')
plt.title('Product Y is Good, Product X is Bad')
plt.xlabel('Product X')
plt.ylabel('Product Y')

# Scenario 4: Product X is good, Product Y is bad
Z4 = utility(-X, Y)
plt.subplot(2, 2, 4)
plt.contourf(X, Y, Z4, levels=20, cmap='coolwarm')
plt.title('Product X is Good, Product Y is Bad')
plt.xlabel('Product X')
plt.ylabel('Product Y')

plt.tight_layout()
plt.show()
