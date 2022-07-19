import numpy as np


# Here, we use Atomic Functions.
def get_mean(list_):
    ''' Compute Mean '''
    print("The mean is {}".format(np.mean(list_)))


def get_max(list_):
    '''Compute Max'''
    print("The max is {}".format(np.max(list_)))


def main(list_):
    # Compute average
    get_mean(list_)

    # Compute max
    get_max(list_)


main([1, 2, 3, 4, 5])

# the mean is 3.0
# the max is 5

'''
1. It is easier to localize errors. Any error in exectuion will point 
   out to a smaller section of your code, accelerating your debug phase.

2. Any part of the code is reusable in other section of your code.

3. Moreover and, often overlooked, is that it is easier to create testing 
   for each function of your code. Side note on testing: You should write
   tests before you actually write the script. 
   But, this is often ignored in favour of creating some nice result 
   to be shown to the stakeholders instead.
'''