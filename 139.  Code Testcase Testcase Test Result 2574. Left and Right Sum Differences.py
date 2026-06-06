class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        left=0
        ans=[]
        for i in range(len(nums)):
            right=total-left-nums[i]
            ans.append(abs(left-right))
            left+=nums[i]
        return ans
