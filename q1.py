from Simplex_tbl import SPLX_tbl
import numpy as np

A = np.array([
    [2,1,1,1,0,0],
    [3,1,2,0,1,0], 
    [1,2,4,0,0,1]])
c = np.array([-500,-250,-600,0,0,0]).T
    #
b = np.array([240,150,180]).T
tbl = SPLX_tbl(6,c,c,A,b)
tbl.solve()