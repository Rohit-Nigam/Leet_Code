class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        left = 0
        for right in range(1,len(nums)):
            print(left,right)
            if nums[left] == nums[right]:
                count += 1
            elif nums[left] != nums[right] and count > 0:
                count = 0
                left += 2
                nums[left] = nums[right]
            elif nums[left]!=nums[right] and count==0:
                left+=1
                nums[left] = nums[right]
        if count>0:
            left+=1
            nums[left]=nums[right]
        return left+1
