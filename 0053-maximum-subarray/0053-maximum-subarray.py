class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=-math.inf
        mx=-math.inf
        for i in range(len(nums)):
            if sum<0:
                sum=0
            sum+=nums[i]
            mx=max(mx,sum)
        return mx