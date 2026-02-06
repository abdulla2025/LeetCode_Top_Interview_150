class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        max_keep = 1
        j = 0
        for i in range(n):
            while j < n and nums[j] <= k * nums[i]:
                j += 1
            max_keep = max(max_keep, j - i)
        return n - max_keep
