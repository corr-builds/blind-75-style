"""
consider that they should be unique - to avoid having to track which outputs we've seen before, we can sort the input array. Then, if a pointer ever moves and has the same value it previously did, we can keep moving it until that is not the case. So, for example, if we have array 1, 3, 3, 5, 6, and we are doing 3sum, and for one iteration we only move the middle pointer (at 3) we would not move it to 3 again - instead we can keep moving it until it reaches 5. Actually, I am still confused about this, because isn't 1,3,3,6 distinct from 1,3,5,6 (in a world where those both added to the same target).

this might relate to three sum. in three sum, you iterate through an array, grabbing pointer "i", and to the right of "i", you do a 2sum problem

how can we use the above 3sum technique to solve 4sum?
well-is it possible to, for each index, do a 3sum problem?
I suppose that for each index, we could do a 3sum problem. I'll try that out

TODO understand why sorting helps us avoid duplicates
solve myself, then solve neetcode way
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    the_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if the_sum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif the_sum > target:
                        r -= 1
                    else:
                        l += 1


        return res
        
