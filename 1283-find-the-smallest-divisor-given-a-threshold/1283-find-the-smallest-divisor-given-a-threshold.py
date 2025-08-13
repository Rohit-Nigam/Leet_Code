class Solution:
    def checksum(self, nums: List[int], threshold: int, divisor: int) -> int:
        total=0
        for i in nums:
            total+=math.ceil(i/divisor)
        return total
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        while(low<=high):
            mid=(low+high)//2
            total=self.checksum(nums,threshold,mid)
            if total<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low