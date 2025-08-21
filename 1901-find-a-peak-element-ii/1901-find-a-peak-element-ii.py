class Solution:
    def check(self, mat: List[List[int]],n:int,m:int,mid:int) -> int:
        maxval=-1
        index=-1
        for i in range(n):
            if mat[i][mid]>maxval:
                maxval=mat[i][mid]
                index=i
        return index
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low=0
        high=m-1
        while(low<=high):
            mid=(low+high)//2
            row=self.check(mat,n,m,mid)
            left = mat[row][mid-1] if mid-1 >= 0 else -1
            right = mat[row][mid+1] if mid+1 < m else -1
            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]
            elif mat[row][mid]<left:
                high=mid-1
            else:
                low=mid+1
        return[-1,-1]