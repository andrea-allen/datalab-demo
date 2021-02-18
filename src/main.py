import matplotlib.pyplot as plt
import numpy as np
from src import dataskills

if __name__ == '__main__':
    print('Main method for Data Lab Demo')

    ############ DEMO ONE #########################
    # Here we have code directly in the main method

    # two_plus_one = 2 + 1
    # magic_math_op = [] #Define an empty list for results
    # for i in range(6):
    #     magic_math_op.append(np.log10(two_plus_one ** i))
    # magic_math_op_as_array = np.array(magic_math_op)
    # range_one_to_ten = np.arange(6)
    # plt.plot(range_one_to_ten, magic_math_op_as_array, color='red', label=f'Base {two_plus_one}')
    #
    # # Repeated code chunk
    # two_plus_three = 2 + 3
    # magic_math_op = []
    # for i in range(6):
    #     magic_math_op.append(two_plus_three ** i) # Same method repeated
    # magic_math_op_as_array = np.array(magic_math_op)
    # range_one_to_ten = np.arange(6)
    # plt.plot(range_one_to_ten, magic_math_op_as_array, color='blue', label=f'Base {two_plus_three}')
    #
    # plt.title('Powers Plot')
    # plt.legend(loc='upper left')
    # plt.show()

    #Here we have code calling some functions pre-defined, in the main file, but not the main method

    # two_plus_one = 2 + 1
    # magic_math_op = []
    # for i in range(6):
    #     magic_math_op.append(dataskills.magic_math_op_method(two_plus_one, i))
    # magic_math_op_as_array = np.array(magic_math_op)
    # range_one_to_ten = np.arange(6)
    # plt.plot(range_one_to_ten, magic_math_op_as_array, color='red', label=f'Base {two_plus_one}')
    #
    # two_plus_three = 2 + 3
    # magic_math_op = []
    # for i in range(6):
    #     magic_math_op.append(dataskills.magic_math_op_method(two_plus_three, i))
    # magic_math_op_as_array = np.array(magic_math_op)
    # range_one_to_ten = np.arange(6)
    # plt.plot(range_one_to_ten, magic_math_op_as_array, color='blue', label=f'Base {two_plus_three}')
    #
    # plt.title('Powers Plot')
    # plt.legend(loc='upper left')
    # plt.show()





    ######### DEMO TWO ##############
    dataskills.covid_data_demo()















