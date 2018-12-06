# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np

def least_squares(y, tx):
    """calculate the least squares."""
    #a = tx.T.dot(tx)
    #b = tx.T.dot(y)
    #return np.linalg.solve(a, b)
    w = np.linalg.inv(tx.T @ tx) @ tx.T @ y
    return 1 / 2 * np.mean((y - tx.dot(w)) ** 2), w
