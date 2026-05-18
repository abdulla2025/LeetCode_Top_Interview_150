class Solution:
    def minJumps(self,nums:List[int])->int:
        valueIndices=defaultdict(list)
        for index,value in enumerate(nums):
            valueIndices[value].append(index)
        queue=deque([0])
        visited={0}
        jumps=0
        while queue:
            for _ in range(len(queue)):
                currentIndex=queue.popleft()
                if currentIndex==len(nums)-1:
                    return jumps
                nextPositions=[currentIndex+1,currentIndex-1,*valueIndices.pop(nums[currentIndex],[])]
                for nextIndex in nextPositions:
                    if 0<=nextIndex<len(nums) and nextIndex not in visited:
                        visited.add(nextIndex)
                        queue.append(nextIndex)
            jumps+=1
