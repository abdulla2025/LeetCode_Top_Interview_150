class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)
        for indices in val_to_indices.values():
            m = len(indices)
            if m == 1:
                continue
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = pref[i] + indices[i]
            for k, idx in enumerate(indices):
                left_sum = idx * k - pref[k]
                right_sum = (pref[m] - pref[k + 1]) - idx * (m - 1 - k)
                ans[idx] = left_sum + right_sum
        return ans
