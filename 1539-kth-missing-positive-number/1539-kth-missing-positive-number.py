class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=len(arr)
        if n==arr[-1]:
            return arr[-1]+k
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            NumberOfMissing=arr[mid]-(mid+1)#as we can see that 4 is on3rd position so only 1 missing number so 4-(2+1)
            if NumberOfMissing>=k:
                high=mid-1
            else:
                low=mid+1
        NumberOfMissing=arr[high]-(high+1)
        print(NumberOfMissing)
        # return arr[high]+k-NumberOfMissing
        return k+high+1