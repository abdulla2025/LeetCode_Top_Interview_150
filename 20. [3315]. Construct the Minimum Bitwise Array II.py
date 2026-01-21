class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(-1)
            else:
                temp = n ^ (n + 1)
                L = (temp >> 1).bit_length()
                r = L - 1
                x = n - (1 << r)
                ans.append(x)
        return ans
