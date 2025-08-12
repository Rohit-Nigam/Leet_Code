class Solution:
    def mySqrt(self, x: int) -> int:
        ans=0
        low=1
        high=x
        while(low<=high):
            mid=(low+high)//2
            if mid**2<=x:
                low=mid+1
                ans=mid
            else:
                high=mid-1
        return ans