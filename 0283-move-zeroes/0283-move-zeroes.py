class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return nums 
        else:
            c=nums.count(0)
            while 0 in nums:
                nums.remove(0)
          
            for i in range(c):
                nums.append(0)
            return nums