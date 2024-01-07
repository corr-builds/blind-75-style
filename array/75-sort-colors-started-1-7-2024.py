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
brainstorming more on a 2 pointer solution:
let's say we do swapping only for 0s and 2s
we can have left and right pointer and idx iterating
good explanation here: https://www.youtube.com/watch?v=R34zEZKO_do

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
        left, right, i = 0, len(nums) - 1, 0

        # now modify in-place
        while i <= right: # we stop when the current index crosses right, because right and everything after will be written since we are writing in-place
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                #i += 1
            else:
                i += 1

        return

    # why does commenting the one line and doing <= instead of < cause the problem to pass?
        # part 1 - why not increment i if equal to 2? so, I think you're starting I from the beginning, but what you ultimately want it to equal is the rightmost barrier of the "middle" section, where the middle section consists of 1s. So I think if it's equal to 0, then of course you'll shift that i pointer over, since you're wanting to get closer to the right side of 1s. And of course if it's a 1, then you can make progress towards that. If it's a 2, however, that only affects the scope of the rightmost category, 2s
        # part 2 - why <= instead of < ? this has to do with the nature of the pointers i and r. i is an inclusive right bound for the 1s. right is an exclusive left bound for the 2s. so if i==right, then you know you'd have ...1, 2... because i is at the last 1, whereas right is also at 1, where on previous iterations it might have sought for an opportunity to swap
