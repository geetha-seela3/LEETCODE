class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                if temp==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                elif temp<0:
                    l+=1
                else:
                    r-=1
                if temp<=0:
                    while l<len(nums) and nums[l]==nums[l-1]:
                        l+=1
        return res















        # nums.sort()
        # res=[]
        # for i in range(len(nums)):
        #     if i>0 and nums[i]==nums[i-1]:
        #         continue
        #     j,k=i+1,len(nums)-1
        #     while j<k:
        #         if nums[i]+nums[j]+nums[k]>0:
        #             k-=1
        #         elif nums[i]+nums[j]+nums[k]<0:
        #             j+=1
        #         else:
        #             sub=[ nums[i] , nums[j] , nums[k] ]
        #             res.append(sub)
        #             j+=1
        #             while j<len(nums) and nums[j]==nums[j-1]:
        #                 j+=1
        # return res



        