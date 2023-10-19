import matplotlib.pyplot as plt
import numpy as np

def plot(func1, func2):
    x = np.linspace(-10, 10, 100)
    y1 = eval(func1)
    y2 = eval(func2)
    plt.plot(x, y1, label='Функция 1')
    plt.plot(x, y2, label='Функция 2')
    plt.grid(True)
    plt.legend()
    plt.show()