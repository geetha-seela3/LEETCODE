class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # TC-->O(n) , sc->O(n)
        hashset=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            res=max(res,r-l+1)
        return res









        # container=set()
        # i=0
        # res=0
        # for j in range(len(s)):
        #     while s[j] in container:
        #         container.remove(s[i])
        #         i+=1
        #     res=max(res,(j-i)+1)
        #     container.add(s[j])
        # return res