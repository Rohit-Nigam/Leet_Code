class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # st = set()
        # n = len(nums)
        # for i in range(n):
        #     nst=set()
        #     for j in range(i+1,n):
        #         reqnum=-(nums[i]+nums[j]) #a+b+c=0   so a=0-(a+b)
        #         if reqnum in nst:
        #             temp=[nums[i],nums[j],reqnum]
        #             temp.sort()
        #             st.add(tuple(temp))
        #         nst.add(nums[j])
        # res = [list(triplet) for triplet in st]
        # return res
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while(j<k):
                sm=nums[i]+nums[j]+nums[k]
                if sm>0:
                    k-=1
                elif sm<0:
                     j+=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while(j<k and nums[j]==nums[j-1]):
                        j+=1
                    while(j<k and nums[k]==nums[k+1]):
                        k-=1
        return res