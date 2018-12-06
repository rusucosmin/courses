# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""

import numpy as np

def split_data(x, y, ratio, seed=1):
    """
    split the dataset based on the split ratio. If ratio is 0.8 
    you will have 80% of your data set dedicated to training 
    and the rest dedicated to testing
    """
    # set seed
    np.random.seed(seed)
    train_size = int(ratio * len(x))
    train_indices = np.random.permutation(len(x))[:train_size]
    test_indices = np.random.permutation(len(x))[train_size:]
    x_train = x[train_indices]
    y_train = y[train_indices]
    x_test = x[test_indices]
    y_test = y[test_indices]
    assert(x_train.shape[0] + x_test.shape[0] == x.shape[0])
    assert(y_train.shape[0] + y_test.shape[0] == y.shape[0])
    return x_train, y_train, x_test, y_test