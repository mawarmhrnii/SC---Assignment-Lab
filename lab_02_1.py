# -*- coding: utf-8 -*-
"""lab-02-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fGXTl8G8KoEiewH16vBM9sb6AiqijNa1
"""

import numpy as np
a = [[8, 3, -3], [-2, -8, 5], [3, 5, 10]]

diag = np.diag(np.abs(a))

off_diag = np.sum(np.abs(a), axis = 1) - diag

if np.all(diag > off_diag):
  print('matrix is diagonally dominant')
else:
  print('NOT diagonally dominant')

x1 = 0
x2 = 0
x3 = 0
epsilon = 0.01
converged = False

x_old = np.array([x1, x2, x3])

print('Iteration results')
print('k,   x1,      x2,      x3')
for k in range(1, 50):
    x1 = (14-3*x2+3*x3)/8
    x2 = (5+2*x1-5*x3)/(-8)
    x3 = (-8-3*x1-5*x2)/(10)
    x = np.array([x1, x2, x3])

    dx = np.sqrt(np.dot(x-x_old, x-x_old))

    print("%d, %.4f, %.4f, %.4f"%(k, x1, x2,x3))
    if dx < epsilon:
        converged = True
        print('Converged!')
        break

    x_old = x

if not converged:
  print('Not converge, increase the # of iterations')
