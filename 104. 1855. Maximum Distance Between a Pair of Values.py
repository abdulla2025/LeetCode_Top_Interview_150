class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        max_dist = 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1:
            if j < i:
                j = i
            while j < n2 and nums1[i] <= nums2[j]:
                j += 1
            if j - 1 >= i:
                max_dist = max(max_dist, j - 1 - i)
            i += 1
        return max_dist
