import matplotlib.pyplot as plt
import numpy as np

def pie(n):
    values = np.random.rand(n)
    plt.figure(figsize=(8, 8))
    plt.pie(values)
    plt.title('Круговая диаграмма с случайными частями')
    plt.legend()
    plt.show()
n = int(input())
pie(n)