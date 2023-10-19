import matplotlib.pyplot as plt
import numpy as np

def randomka():
    random_values = np.random.rand(7)
    x = np.arange(7)
    plt.bar(x, random_values)
    plt.title('Столбчатый график с случайными значениями')
    plt.xlabel('Столбцы')
    plt.ylabel('Значения')
    plt.grid(True)
    plt.show()
randomka()