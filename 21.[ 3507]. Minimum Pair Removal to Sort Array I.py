class Solution:
    def minimumPairRemoval(self, nums):
        def is_non_decreasing(arr):
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True
        
        arr = nums[:]
        ops = 0
        while not is_non_decreasing(arr):
            min_sum = float('inf')
            min_idx = 0
            for i in range(len(arr) - 1):
                s = arr[i] + arr[i+1]
                if s < min_sum:
                    min_sum = s
                    min_idx = i
            arr = arr[:min_idx] + [min_sum] + arr[min_idx+2:]
            ops += 1
        return ops
