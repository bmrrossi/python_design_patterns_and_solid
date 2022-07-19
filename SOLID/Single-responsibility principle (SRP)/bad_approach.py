import numpy as np

# All operations are into that method. This is not good.
# A better approach is divide the math operations in atomic functions
def math_operations(list_):
    # Compute Average
    print("The mean is {}".format(np.mean(list_)))
    # Compute Max
    print("The max is {}".format(np.max(list_)))


math_operations(list_ = [1, 2, 3, 4, 5])
# the mean is 3.0
# the max is 5