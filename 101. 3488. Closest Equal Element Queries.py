class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n=len(nums)
        pos=collections.defaultdict(list)
        for i,v in enumerate(nums):
            pos[v].append(i)
        best=[-1]*n
        for v,arr in pos.items():
            m=len(arr)
            if m==1:
                continue
            for k in range(m):
                i=arr[k]
                p=arr[k-1]
                q=arr[(k+1)%m]
                d1=abs(i-p)
                d1=min(d1,n-d1)
                d2=abs(i-q)
                d2=min(d2,n-d2)
                best[i]=min(d1,d2)
        return [best[i] for i in queries]