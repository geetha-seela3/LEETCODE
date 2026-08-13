class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort()
        n = len(res)
        if n == 0:
            return None  
        mid = n // 2
        if n % 2 == 1:
            return (res[mid])
        else:
            return (res[mid - 1] + res[mid])/2.0
        