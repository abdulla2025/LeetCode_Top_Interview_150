class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        
        seen = {}
        ans = float('inf')
        
        for i, x in enumerate(nums):
            if x in seen:
                ans = min(ans, i - seen[x])
            seen[rev(x)] = i
            
        return ans if ans != float('inf') else -1
