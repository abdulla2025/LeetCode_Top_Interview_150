class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        pair_sums = SortedList()
        active_indices = SortedList(range(n))
        inversion_count = 0
        for i in range(n - 1):
            pair_sums.add((nums[i] + nums[i + 1], i))
            if nums[i] > nums[i + 1]:
                inversion_count += 1
        operations = 0
        while inversion_count:
            operations += 1
            merged_value, current_idx = pair_sums.pop(0)
            pos_in_active = active_indices.index(current_idx)
            next_idx = active_indices[pos_in_active + 1]
            if nums[current_idx] > nums[next_idx]:
                inversion_count -= 1
            if pos_in_active > 0:
                left_idx = active_indices[pos_in_active - 1]
                
                if nums[left_idx] > nums[current_idx]:
                    inversion_count -= 1
                
                pair_sums.remove((nums[left_idx] + nums[current_idx], left_idx))
                
                if nums[left_idx] > merged_value:
                    inversion_count += 1
                
                pair_sums.add((nums[left_idx] + merged_value, left_idx))
            
            if pos_in_active + 2 < len(active_indices):
                right_idx = active_indices[pos_in_active + 2]
                
                if nums[next_idx] > nums[right_idx]:
                    inversion_count -= 1
                
                pair_sums.remove((nums[next_idx] + nums[right_idx], next_idx))
                
                if merged_value > nums[right_idx]:
                    inversion_count += 1
                
                pair_sums.add((merged_value + nums[right_idx], current_idx))
            
            nums[current_idx] = merged_value
            active_indices.remove(next_idx)
        
        return operations
