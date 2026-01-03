class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        type_a = 6
        type_b = 6  
    
        for i in range(2, n + 1):
            new_type_a = (type_a * 3 + type_b * 2) % MOD
            new_type_b = (type_a * 2 + type_b * 2) % MOD
            type_a = new_type_a
            type_b = new_type_b
        
        return (type_a + type_b) % MOD