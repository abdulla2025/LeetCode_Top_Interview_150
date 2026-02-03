class Solution:
    def isTrionic(self,nums)->bool:
        n=len(nums)
        for p in range(1,n-2):
            for q in range(p+1,n-1):
                v=True
                for i in range(p):
                    if nums[i]>=nums[i+1]:
                        v=False
                        break
                if not v:
                    continue
                for i in range(p,q):
                    if nums[i]<=nums[i+1]:
                        v=False
                        break
                if not v:
                    continue
                for i in range(q,n-1):
                    if nums[i]>=nums[i+1]:
                        v=False
                        break
                if v:
                    return True
        return False
