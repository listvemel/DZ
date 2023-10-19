import matplotlib.pyplot as plt
import numpy as np


def plot_four_functions():
    x = np.linspace(0.1, 10, 400)
    y1 = np.cos(x)
    y2 = np.sin(x)
    y3 = x**2
    y4 = 2 / x
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(x, y1)
    plt.title('График cos(x)')
    plt.grid(True)
    
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, color='red')
    plt.title('График sin(x)')
    plt.grid(True)
    
    plt.subplot(2, 2, 3)
    plt.plot(x, y3, color='green')
    plt.title('График x^2')
    plt.grid(True)
    
    plt.subplot(2, 2, 4)
    plt.plot(x, y4, color='purple')
    plt.title('График 2/x')
    plt.grid(True)
    
    plt.subplot(2, 2, 1)
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.subplot(2, 2, 2)
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.subplot(2, 2, 3)
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.subplot(2, 2, 4)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

    
plot_four_functions()