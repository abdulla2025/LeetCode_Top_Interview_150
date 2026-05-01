class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        total = sum(nums)
        curr = sum(i * nums[i] for i in range(n))
        ans = curr
        
        for i in range(1, n):
            curr = curr + total - n * nums[n - i]
            ans = max(ans, curr)
        
        return ans
