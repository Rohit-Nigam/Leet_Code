class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        l=[]
        s=set(arr)
        for i in s:
            l.append(arr.count(i))
        if(len(l)==len(set(l))):
            return True
        else:
            return False