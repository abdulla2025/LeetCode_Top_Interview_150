class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        total_initial_energy = current_energy = 0

        for actual_cost, min_required in sorted(tasks, key=lambda x: x[0] - x[1]):
            if current_energy < min_required:
                deficit = min_required - current_energy
                total_initial_energy += deficit
                current_energy = min_required
            current_energy -= actual_cost
        
        return total_initial_energy
 
