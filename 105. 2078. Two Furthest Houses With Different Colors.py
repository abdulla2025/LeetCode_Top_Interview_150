class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n=len(colors)
        a=0
        for i in range(n-1,-1,-1):
            if colors[i]!=colors[0]:
                a=i
                break
        for i in range(n):
            if colors[i]!=colors[-1]:
                a=max(a,n-1-i)
                break
        return a