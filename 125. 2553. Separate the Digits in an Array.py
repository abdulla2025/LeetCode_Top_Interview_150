class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            num_str = str(num)
            for digit_char in num_str:
                result.append(int(digit_char))
        
        return result
