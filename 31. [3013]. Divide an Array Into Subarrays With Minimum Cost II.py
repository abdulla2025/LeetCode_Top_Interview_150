class Solution:
    def minimumCost(self,nums,k:int,dist:int)->int:
        def a2b():
            nonlocal t
            v=a.pop()
            t-=v
            b.add(v)
        def b2a():
            nonlocal t
            v=b.pop(0)
            a.add(v)
            t+=v
        k-=1
        t=sum(nums[:dist+2])
        a=SortedList(nums[1:dist+2])
        b=SortedList()
        while len(a)>k:
            a2b()
        m=t
        for i in range(dist+2,len(nums)):
            x=nums[i-dist-1]
            if x in a:
                a.remove(x)
                t-=x
            else:
                b.remove(x)
            y=nums[i]
            if y<a[-1]:
                a.add(y)
                t+=y
            else:
                b.add(y)
            while len(a)<k:
                b2a()
            while len(a)>k:
                a2b()
            m=min(m,t)
        return m
