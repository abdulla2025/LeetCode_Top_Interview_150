class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            temp = n
            trailing_ones = 0
            while temp & 1:
                trailing_ones += 1
                temp >>= 1
            
            min_x = float('inf')
            for L in range(1, trailing_ones + 1):
                x = (n & ~((1 << L) - 1)) + (1 << (L - 1)) - 1
                min_x = min(min_x, x)
            
            ans.append(min_x)
        
        return ans
