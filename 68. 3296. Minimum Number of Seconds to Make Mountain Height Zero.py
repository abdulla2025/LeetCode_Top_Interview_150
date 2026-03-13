class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def all_workers_done(seconds_elapsed: int) -> bool:
            height_reduced_so_far = 0
            for time_per_unit in workerTimes:
                height_reduced_so_far += int(sqrt(2 * seconds_elapsed / time_per_unit + 1 / 4) - 1 / 2)
            return height_reduced_so_far >= mountainHeight

        return bisect_left(range(10**16), True, key=all_workers_done)
