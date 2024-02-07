class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre=[[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 and j ==0:
                    self.pre[i][j] = matrix[i][j]
                elif i == 0 and j!=0:
                    self.pre[i][j] = self.pre[i][j-1] + matrix[i][j]
                elif i!=0 and j==0:
                    self.pre[i][j] = self.pre[i-1][j] +matrix[i][j]
                else:
                    self.pre[i][j] = self.pre[i-1][j] + self.pre[i][j-1] - self.pre[i-1][j-1]+matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1==0 and col1==0:
            return self.pre[row2][col2]
        elif row1 ==0 and col1!=0:
            return self.pre[row2][col2] - self.pre[row2][col1-1]
        elif row1!=0 and col1==0:
            return self.pre[row2][col2] - self.pre[row1-1][col2]
        else:
            return self.pre[row2][col2] - self.pre[row2][col1-1] - self.pre[row1-1][col2]+self.pre[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)