class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mindex=0
        for i in range(len(nums)):
            if i>mindex :
                return False
            mindex=max(mindex,i+nums[i])
        return True