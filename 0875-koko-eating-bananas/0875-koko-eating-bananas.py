class Solution:
    def time(self, piles: List[int], mid: int) -> int:
        ans=0
        for i in (piles):
            ans+=math.ceil(i/mid)
        print(ans)
        return ans
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        print(high)
        while(low<=high):
            mid=(low+high)//2
            print("mid",mid)
            timetaken=self.time(piles,mid)
            if timetaken<=h:
                high=mid-1
            else:
                low=mid+1
        return low