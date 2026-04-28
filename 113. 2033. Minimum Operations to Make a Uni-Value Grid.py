class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        nums.sort()
        n = len(nums)
        median = nums[n // 2]
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations
