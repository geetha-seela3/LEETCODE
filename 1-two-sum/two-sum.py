class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap --> tc== O(n) , sc ==O(n)
        hashmap={}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [i,hashmap[target-nums[i]]]
            hashmap[nums[i]]=i

        # hashmap={}
        # for i in range(len(nums)):
        #     rem=(target-nums[i])
        #     if rem in hashmap:
        #         return [hashmap[rem],i]
        #     hashmap[nums[i]]=i
            

       
#bruteforce--> tc= O(n^2), sc==O(1)
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        # return nums

        # nums.sort()
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     if nums[i]+nums[j]>target:
        #         j-=1
        #     elif nums[i]+nums[j]<target:
        #         i+=1
        #     else:
        #         return [i,j]

        #     # if nums[i]+nums[j]==target:
        #     #     return [i,j]
