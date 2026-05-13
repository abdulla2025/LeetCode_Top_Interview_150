class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 3)
        
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            

            if a > b:
                a, b = b, a
            delta[2] += 2
            delta[2 * limit + 1] -= 2
            delta[a + 1] -= 1
            delta[b + limit + 1] += 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
        moves = 0
        min_moves = float('inf')
        
        for target in range(2, 2 * limit + 1):
            moves += delta[target]
            min_moves = min(min_moves, moves)
        
        return min_moves
