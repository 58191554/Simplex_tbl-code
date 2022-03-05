from Simplex_tbl import SPLX_tbl
import numpy as np

#
A = np.array([
    [1 ,0 , 0,4 , 1 ],
    [0 ,1 , 0,-7, 0 ],
    [0 ,0 , 1,4/3 , 1/3 ]])
n = 5
c = np.array([2,3,3,1,-2]).T
b = np.array([2,0,1]).T
reduced_cost = np.array([0,0,0,3,-5]).T
tbl = SPLX_tbl(n,c,reduced_cost,A,b, 7)
tbl.solve()