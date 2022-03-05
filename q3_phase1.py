from Simplex_tbl import SPLX_tbl
import numpy as np

#
A = np.array([
    [1 , 3, 0,4 , 1, 1, 0, 0 ],
    [1 , 2, 0,-3, 1, 0, 1, 0 ],
    [-1,-4, 3,0 , 0, 0, 0, 1]])
n = 8
c = np.array([0,0,0,0,0,1,1,1]).T
b = np.array([2,2,1]).T
reduced_cost = np.array([-1,-1,-3,-1,-2,0,0,0]).T
tbl = SPLX_tbl(n,c,reduced_cost,A,b, -5)
tbl.solve()