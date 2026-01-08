class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                product = nums1[i-1] * nums2[j-1]
                
                take_current = product
                if dp[i-1][j-1] != float('-inf'):
                    take_current = max(take_current, dp[i-1][j-1] + product)
                
                skip_first = dp[i-1][j]
                
                skip_second = dp[i][j-1]
                
                dp[i][j] = max(take_current, skip_first, skip_second)
        
        return dp[m][n]