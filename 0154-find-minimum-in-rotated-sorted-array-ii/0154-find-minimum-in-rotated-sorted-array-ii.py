class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        low=0
        high=n-1
        ans=math.inf
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==nums[low] and nums[mid]==nums[high]:
                ans=min(ans,nums[low])
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ans=min(ans,nums[mid])
                high=mid-1
        return ans