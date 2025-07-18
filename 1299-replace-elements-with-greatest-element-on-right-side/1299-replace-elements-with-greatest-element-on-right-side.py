class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx=-1
        res=[]
        for i in range(len(arr)-1,-1,-1):
            res.append(mx)
            mx=max(arr[i],mx)
        return res[-1::-1]