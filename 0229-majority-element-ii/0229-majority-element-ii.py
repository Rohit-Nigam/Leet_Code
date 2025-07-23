class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(len(nums)//3)
        res=[]
        for i in range(len(nums)):
            if len(res)==0 or res[-1]!=nums[i]:
                count=0
                for j in range(i,len(nums)):
                    if nums[j]==nums[i]:
                        count+=1
                    if count>len(nums)//3:
                        res.append(nums[i])
                        break
        return res