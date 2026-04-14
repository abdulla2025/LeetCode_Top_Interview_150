class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        @cache
        def assignRobots(robotIndex, factoryIndex):
            if robotIndex == len(robot):
                return 0
            if factoryIndex == len(factory):
                return inf
            minimumDistance = assignRobots(robotIndex, factoryIndex + 1)
            accumulatedDistance = 0
            for assignedCount in range(factory[factoryIndex][1]):
                if robotIndex + assignedCount == len(robot):
                    break
                accumulatedDistance += abs(robot[robotIndex + assignedCount] - factory[factoryIndex][0])
                minimumDistance = min(minimumDistance, accumulatedDistance + assignRobots(robotIndex + assignedCount + 1, factoryIndex + 1))
            return minimumDistance

        robot.sort()
        factory.sort()
        result = assignRobots(0, 0)
        assignRobots.cache_clear()
        return result
