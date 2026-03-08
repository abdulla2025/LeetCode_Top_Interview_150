class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = ""
        for i in range(len(nums)):
            if nums[i][i] == "1":
                result += "0"
            else:
                result += "1"
        return result
