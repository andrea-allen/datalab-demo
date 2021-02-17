import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    print('Main method for Data Lab Demo')
    two_plus_one = 2 + 1
    powers = []
    for i in range(10):
        powers.append(two_plus_one ** i)
    powers_as_array = np.array(powers)
    range_one_to_ten = np.arange(10)
    plt.scatter(range_one_to_ten, powers_as_array, color='red')
    plt.title('Powers Plot')
    plt.show()