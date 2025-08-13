class Solution:
    def check(self, bloomDay: List[int], day: int, m: int, k: int) -> int:
        ans=0
        count=0
        for i in bloomDay:
            if i<=day:
                count+=1
            else:
                ans+=count//k
                count=0
        ans+=count//k
        return ans>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while(low<=high):
            mid=(low+high)//2
            print(mid)
            if (self.check(bloomDay,mid,m,k)):
                high=mid-1
            else:
                low=mid+1
        return low