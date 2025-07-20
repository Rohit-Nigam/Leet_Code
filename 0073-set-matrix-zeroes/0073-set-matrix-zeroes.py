class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix) #Number of row 
        n=len(matrix[0]) #Number of column
        col=[0]*n
        row=[0]*m
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    col[j]=1
                    row[i]=1
        for i in range(m):
            for j in range(n):
                if col[j] or row[i]:
                    matrix[i][j]=0
        return matrix