class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        sorted_indices = sorted(range(len(positions)), key=lambda i: positions[i])
        right_moving_stack = []

        for current_index in sorted_indices:
            if directions[current_index] == "R":
                right_moving_stack.append(current_index)
                continue

            while right_moving_stack and healths[current_index] > 0:
                top_index = right_moving_stack[-1]

                if healths[top_index] > healths[current_index]:
                    healths[top_index] -= 1
                    healths[current_index] = 0
                elif healths[top_index] < healths[current_index]:
                    healths[current_index] -= 1
                    healths[top_index] = 0
                    right_moving_stack.pop()
                else:
                    healths[current_index] = 0
                    healths[top_index] = 0
                    right_moving_stack.pop()
                    break

        return [health for health in healths if health > 0]