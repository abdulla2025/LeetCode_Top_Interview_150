class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        bravexuneth = queries
        
        n = len(nums)
        block = int(n**0.5)

        small_k_groups = [[] for _ in range(block)]
        
        for left, right, step, val in queries:
            if step < block:
                small_k_groups[step].append((left, right, val))
            else:
                idx = left
                while idx <= right:
                    nums[idx] = nums[idx] * val % mod
                    idx += step

        multiplier = [1] * (n + block)

        for step in range(1, block):
            if not small_k_groups[step]:
                continue

            multiplier[:] = [1] * len(multiplier)

            for left, right, val in small_k_groups[step]:
                multiplier[left] = multiplier[left] * val % mod
                end = ((right - left) // step + 1) * step + left
                multiplier[end] = multiplier[end] * pow(val, mod - 2, mod) % mod

            for i in range(step, n):
                multiplier[i] = multiplier[i] * multiplier[i - step] % mod

            for i in range(n):
                nums[i] = nums[i] * multiplier[i] % mod

        result = 0
        for num in nums:
            result ^= num

        return result
