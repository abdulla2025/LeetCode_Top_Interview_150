class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s=set()
        for x in arr1:
            while x>0:
                s.add(x)
                x//=10
        ans=0
        for y in arr2:
            while y>0:
                if y in s:
                    ans=max(ans,len(str(y)))
                y//=10
        return ans
