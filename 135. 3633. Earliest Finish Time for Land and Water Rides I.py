class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        earliest=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_first=max(landStartTime[i],0)+landDuration[i]
                water_second=max(waterStartTime[j],land_first)+waterDuration[j]
                earliest=min(earliest,water_second)
                water_first=max(waterStartTime[j],0)+waterDuration[j]
                land_second=max(landStartTime[i],water_first)+landDuration[i]
                earliest=min(earliest,land_second)
        return earliest
