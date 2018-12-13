# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""
import numpy as np

def least_squares(y, tx):
    """calculate the least squares."""
    a = tx.T.dot(tx)
    b = tx.T.dot(y)
    w = np.linalg.solve(a, b)
    err = ((y - tx.dot(w)) ** 2).mean()
    return err, w
