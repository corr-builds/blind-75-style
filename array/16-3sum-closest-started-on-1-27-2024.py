"""
when you find a sum, how do you know which is the closestt to target?
each time, just ask is it closer
it's closer if the difference between the sum and target is smaller than the current shortes diff b/t sum and target

instead of storing diff, let's just store the three nums and calculate each time to find if new triplet has smaller diff

I can think of this as like 3sum, except with more to track
in regular 3sum, you return immediately when you find equality
in this problem, we could only return immediately if target were equal to sum
for all other cases, we would want to store only the 3 numbers with the smallest difference
and then we could still use two pointer for the internal 2sum problem - decreasing if sum is greater than target, and increasing if it is less

a + b + c = target
b + c = target - a
"""
# todo - compare with fast solution, and figure out why faster
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest_diff = float('inf')
        smallest_sum = None
        nums.sort()
        # iterate over nums
        for i in range(len(nums) - 2):
            j, h = i + 1, len(nums) - 1
            current_target = target - nums[i]
            while j < h:
                current_sum = nums[j] + nums[h]
                if current_sum == current_target:
                    return current_sum + nums[i]
                current_diff = abs(target - nums[i] - current_sum)
                if current_diff < smallest_diff:
                    smallest_diff = current_diff
                    smallest_sum = current_sum + nums[i]
                if current_sum + nums[i] > target:
                    h -= 1
                else:
                    j += 1

        return smallest_sum
