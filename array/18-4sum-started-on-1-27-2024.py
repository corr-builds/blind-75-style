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
        nums.sort()
        res, quad = [], [] # I think quad is the current quadruplet

        def kSum(k, start, target):
            if k != 2: # not the base case. k == 2 is the base case, because in that case it simplifies down to a 2sum - input array is sorted problem
                for i in range(start, len(nums) - k + 1): # - k + 1 because in the case of 3sum, for example, we go until there are 2 spaces remaining to allow room for the 2 additional pointers
                    if i > start and nums[i] == nums[i - 1]: # since we don't want duplicates, we can prevent any one pointer from moving to a spot which is not meaninful to our answer (e.g. if we have pointers at 1, 1, 2, 3 and the pointer at 2 also has a 2 adjacent to it and so moves to make 1, 1, 2, 3 again, that would be wasted compute, so skip to the next thing that i can point at)
                        continue
                    quad.append(nums[i]) # add the value at i to the current quadruplet
                    kSum(k - 1, i + 1, target - nums[i]) # recursive call. I'll explain the arguments from right to left. having a candidate for the first element in the quadruplet, we can now reduce the target by the amount of that candidate (target - nums[i]). for the second argument (i + 1) we want to start at iterating at one place past the place that is currently taken by our pointer (i). And, for the first argument (k - 1) since we already have used one pointer, the problem now becomes a problem of checking equality amongst 1 less pointers. This call will recurse until it hits the base case where k==2
                    quad.pop() # remove the last item from the list. pop the value we just added in the line before the previous line, doing clean-up. this works because we recurse all the way down to the base case in the previous line, either adding or not addding a valid quadruplet. Once we've gotten our valid quadruplet (or not), we do want to clean up our quad array before the next iteration. considering the clean-up from the perspective of the recursion (rather than the iteration) imagine that we have reached the base case and are starting to clean frames off of the recursive function stack, and right before each of those methods returns, it cleans up one element from the quad array (the one it added)
                    # side point related to the above comment - we are making a recursive call inside of an iterative loop. how do this iteration and this recursion relate to each other in this algorithm? well, one way to think of it is: within a recursive call, we are going to iterate from the start to the end, allowing room for remaining pointers at the end. within that iteration (for each pointer we select) we are going to make a recursive call which decreases the number of pointers used until we reach the base case. after that recursive call (after each recursive step, you might think) we clean up the pointer that we had selected and added to the quad array for that specific layer of recursion
                return # you can return from the method once you've finished your iteration
            # base case
            l, r = 0, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1 # arbitrarily move l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0, target)
        return res
                    # todo code identical to neetcodes (i think) and not passing, cross-compare with other solutions
        
