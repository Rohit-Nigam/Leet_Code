class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mpp = {}
        res = []
        for i in nums:
            if len(res)==2:
                break
            mpp[i] = mpp.get(i, 0) + 1
            if mpp[i] > (len(nums) // 3) and i not in res:
                res.append(i)
        return res