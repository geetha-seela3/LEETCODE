class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # tc->O(n) , sc->
        max_len=0
        hashset=set(nums)
        for n in hashset:
            if (n-1) not in hashset:
                c=1
                while (n+c) in hashset:
                    c+=1
                max_len=max(max_len,c)
        return max_len
        

















        # hash=set(nums)
        # res=0
        # for num in hash:
        #     if (num-1) not in hash:
        #         count=0
        #         while (num+count) in hash:
        #             count+=1
        #         res=max(count,res)
        # return res



        