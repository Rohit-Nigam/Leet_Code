class Solution:
    def first(self, nums: List[int], target: int) -> int:
        n=len(nums)
        firstocr=-1
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                firstocr=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return firstocr
    def last(self, nums: List[int], target: int) -> int:
        n=len(nums)
        second=-1
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                second=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return second
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=self.first(nums,target)
        if start==-1:
            return [-1,-1]
        end=self.last(nums,target)
        return [start,end]