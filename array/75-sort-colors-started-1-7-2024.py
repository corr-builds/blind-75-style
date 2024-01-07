"""
clarify:
straightforward problem statement

input:
nums - objects of color: red, white, or blue
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

output:
nums in-place ordered so objects of same color adjacent in order red, white, blue

edge case:
size is 1

strategy:
use two-pointer
have one pointer to write and another pointer to read
increment write on each pass
on each pass:
hmm, todo
one idea would be to swap write and read if applicable like so:
[2, 1, 0, 1]
swap 1 and 2
[1, 2, 0, 1]
actually, I think I have an idea that doesn't use two pointer
we could pass through the array with a hashmap to counter the number of 0s, 1s, and 2s
then, simply fill that number of 0s, 1s, and 2s into the array

test:
[2, 1, 0, 1]
store nums to counts
populate 1 0
populate 2 1
populate 1 2

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        # now modify in-place
        for i, num in enumerate(nums):
            if counts[0] != 0:
                nums[i] = 0
                counts[0] -= 1
            elif counts[1] != 0:
                nums[i] = 1
                counts[1] -= 1
            else:
                nums[i] = 2

        return
        
