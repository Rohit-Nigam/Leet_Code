class Solution:
    def checkweights(self, weights: List[int], limitdays: int, weightperday: int) -> int:
        day=1
        totalweight=0
        for i in weights:
            totalweight+=i
            if totalweight>weightperday:
                totalweight=i
                day+=1
        return day<=limitdays
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while(low<=high):
            mid=(low+high)//2
            if (self.checkweights(weights,days,mid)):
                high=mid-1
            else:
                low=mid+1
        return low