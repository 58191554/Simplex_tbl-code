from Simplex_tbl import SPLX_tbl
import numpy as np

#
A = np.array([
    [-2,-9,1,9,1,0],
    [1/3,1,-1/3,-2,0,1]])
n = 6
c = np.array([0,0,0,1,1,1]).T
b = np.array([0,0]).T
reduced_cost = np.array([5/3,8,-2/3,-7,0,0]).T
tbl = SPLX_tbl(n,c,reduced_cost,A,b, 0)
tbl.solve()