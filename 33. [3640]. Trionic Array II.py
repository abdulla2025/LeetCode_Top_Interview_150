class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        current_index = 0
        max_sum = -float('inf')
        while current_index < n:
            start_index = current_index
            current_index += 1
            while current_index < n and nums[current_index - 1] < nums[current_index]:
                current_index += 1
            if current_index == start_index + 1:
                continue
            peak_index = current_index - 1
            current_sum = nums[peak_index - 1] + nums[peak_index]
            while current_index < n and nums[current_index - 1] > nums[current_index]:
                current_sum += nums[current_index]
                current_index += 1
            if current_index == peak_index + 1 or current_index == n or nums[current_index - 1] == nums[current_index]:
                continue
            valley_index = current_index - 1
            current_sum += nums[current_index]
            current_index += 1
            max_suffix_sum = suffix_sum = 0
            while current_index < n and nums[current_index - 1] < nums[current_index]:
                suffix_sum += nums[current_index]
                current_index += 1
                max_suffix_sum = max(max_suffix_sum, suffix_sum)
            current_sum += max_suffix_sum
            max_prefix_sum = prefix_sum = 0
            for j in range(peak_index - 2, start_index - 1, -1):
                prefix_sum += nums[j]
                max_prefix_sum = max(max_prefix_sum, prefix_sum)
            current_sum += max_prefix_sum
            max_sum = max(max_sum, current_sum)
            current_index = valley_index
        return max_sum
