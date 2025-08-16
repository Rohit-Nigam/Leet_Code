class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count=0
        n=len(nums1)+len(nums2)
        index2=n//2
        index1=index2-1
        elem1=-1
        elem2=-1
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                if count==index1:
                    elem1=nums1[i]
                if count==index2:
                    elem2=nums1[i]
                count+=1
                i+=1
            else:
                if count==index1:
                    elem1=nums2[j]
                if count==index2:
                    elem2=nums2[j]
                count+=1
                j+=1
        while(i<len(nums1)):
                if count==index1:
                    elem1=nums1[i]
                if count==index2:
                    elem2=nums1[i]
                count+=1
                i+=1
        while(j<len(nums2)):
                if count==index1:
                    elem1=nums2[j]
                if count==index2:
                    elem2=nums2[j]
                count+=1
                j+=1
        if n%2==1:
            return elem2
        return (elem1+elem2)/2