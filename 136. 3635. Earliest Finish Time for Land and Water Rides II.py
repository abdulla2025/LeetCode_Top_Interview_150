class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(a1, t1, a2, t2):
            minEnd = float('inf')
            for i in range(len(a1)):
                minEnd = min(minEnd, a1[i] + t1[i])
            ans = float('inf')
            for i in range(len(a2)):
                ans = min(ans, max(minEnd, a2[i]) + t2[i])
            return ans
        
        x = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        y = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(x, y)
