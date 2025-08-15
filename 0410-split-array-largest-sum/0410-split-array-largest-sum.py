class Solution:
    def check(self, nums: List[int],limit: int, k: int) -> int:
        count=1
        total=0
        for i in nums:
            if total+i<=limit:
                total+=i
            else:
                total=i
                count+=1
        return count

    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        while(low<=high):
            mid=(low+high)//2  
            if self.check(nums,mid,k)>k:
                low=mid+1
            else:
                high=mid-1
        return low