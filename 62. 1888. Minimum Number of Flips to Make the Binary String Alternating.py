class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled = s + s
        alt1 = "".join(str(i % 2) for i in range(2 * n))
        alt2 = "".join(str((i + 1) % 2) for i in range(2 * n))
        
        result = float('inf')
        mismatch1 = mismatch2 = 0
        left = 0
        
        for right in range(2 * n):
            if doubled[right] != alt1[right]:
                mismatch1 += 1
            if doubled[right] != alt2[right]:
                mismatch2 += 1
            
            if right - left + 1 > n:
                if doubled[left] != alt1[left]:
                    mismatch1 -= 1
                if doubled[left] != alt2[left]:
                    mismatch2 -= 1
                left += 1
            
            if right - left + 1 == n:
                result = min(result, mismatch1, mismatch2)
        
        return result
