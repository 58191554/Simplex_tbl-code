import numpy as np 
import sys

class SPLX_tbl:
    def __init__(self,  x_dimension:int, c:np.ndarray,reduced_cost:np.ndarray, A:np.ndarray, b:np.ndarray, op_val = 0):
        self.c = c.copy()
        self.A = A.copy()
        self.x_dim = x_dimension
        self.reduced_cost = reduced_cost.copy()
        self.op_val = op_val
        self.x_B = b.copy()
        self.left_lower = A.copy()

    def get_table(self):
        print("reduced_cost", end="")
        print(self.reduced_cost)
        print("left_lower")
        print(self.left_lower)
        print("op_val: ", end="")
        print(self.op_val)
        print("x_B",end="")
        print(self.x_B)
        print("="*50)

    def find_column(self):  #according to bland's rule , find the first negative one as pivot column
        for j in range(len(self.reduced_cost)):
            if self.reduced_cost[j] < 0:
                return j
        return -1           #cannot find a negative column, optimal case , return -1

    def find_row(self,column):                  #according to the minimal ratio rule
        pivot_column = self.left_lower[:,column]
        print("pivot_column", pivot_column)
        print("x_B" , self.x_B)
        ratio_arr = self.x_B/pivot_column
        ratio_arr:np.ndarray
        print("ratio_arr: ", ratio_arr)         #calculate the reduced ratio and find the smallest one 
        minimal_ratio = sys.maxsize
        minimal_idx = -1
        for i in range(len(ratio_arr)):
            if  ratio_arr[i]<minimal_ratio and ratio_arr[i]>0:
                minimal_ratio = ratio_arr[i]
                minimal_idx = i
        #print("minimal ratio:", minimal_ratio)
        #print("minimal_idx", minimal_idx)

        return minimal_idx

    def operate(self):
        j = self.find_column()
        if j == -1:
            print("Terminal optimal!!")
            return -1
        i = self.find_row(j)
        print("pivot index: ", i, j)

        pivot = self.left_lower[i,j]

        #update the left lower
        pivot_row = self.left_lower[i,:] / pivot                #normalized the pivot row:
        pivot_x_B = self.x_B[i] / pivot
        new_left_lower = np.ndarray(shape=(self.x_B.shape[0], self.x_dim))
        new_left_lower[i,:] = pivot_row

        new_x_B = np.ndarray(shape=(self.x_B.shape[0],1))

        print("pivot_row",pivot_row)

        for row in range(len(new_left_lower)):
            if row == i:
                continue
            else:
                w = -self.left_lower[row,j]
                new_left_lower[row,:] = self.left_lower[row,:] + w*pivot_row

                new_x_B[row] = self.x_B[row] + w*pivot_x_B

        #assign new value into the table
        self.left_lower = new_left_lower
        self.x_B = new_x_B.reshape(self.x_B.shape)
        self.op_val = self.op_val - self.reduced_cost[j]*pivot_x_B
        self.reduced_cost = self.reduced_cost - self.reduced_cost[j]*pivot_row

        #print("new left lower is: ")
        #print(self.left_lower)
        #print("the new x_B is : ")
        #print(self.x_B)
        #print("opval", self.op_val)
        #print("reduced cost", self.reduced_cost)
        pass

    def solve(self):
        while self.find_column()!=-1:
            self.operate()
            self.get_table()
        pass


if __name__ == "__main__":
    #prob 1
    #A = np.array([
    #    [2,1,1,1,0,0],
    #    [3,1,2,0,1,0], 
    #    [1,2,4,0,0,1]])
    #c = np.array([-500,-250,-600,0,0,0]).T
    #
    #b = np.array([240,150,180]).T
    #tbl = SPLX_tbl(6,c,c,A,b)
    #tbl.solve()

    #prob 3.auxilary
    A = np.array([
        [1 , 3, 0,4 , 1, 1, 0, 0 ],
        [1 , 3, 0,-3, 1, 0, 1, 0 ],
        [-1,-4, 3,0 , 0, 0, 0, 1]])
    n = 8
    c = np.array([0,0,0,0,0,1,1,1]).T
    b = np.array([2,2,1]).T
    reduced_cost = np.array([-1,-1,-3,-1,-2,0,0,0]).T
    tbl = SPLX_tbl(n,c,reduced_cost,A,b)
    tbl.solve()

   
