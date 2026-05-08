maxx = 10**6 + 1
factors = []
for _ in range(maxx):
    factors.append([])

for prime in range(2, maxx):
    if not factors[prime]:
        for multiple in range(prime, maxx, prime):
            factors[multiple].append(prime)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        length = len(nums)
        factor_to_indices = defaultdict(list)

        for index, value in enumerate(nums):
            for prime_factor in factors[value]:
                factor_to_indices[prime_factor].append(index)

        steps = 0
        visited = [False] * length
        visited[0] = True
        current_level = [0]

        while True:
            next_level = []

            for current_index in current_level:
                if current_index == length - 1:
                    return steps

                reachable_indices = factor_to_indices[nums[current_index]]
                reachable_indices.append(current_index + 1)

                if current_index > 0:
                    reachable_indices.append(current_index - 1)

                for next_index in reachable_indices:
                    if 0 <= next_index < length and not visited[next_index]:
                        visited[next_index] = True
                        next_level.append(next_index)

                reachable_indices.clear()

            current_level = next_level
            steps += 1
