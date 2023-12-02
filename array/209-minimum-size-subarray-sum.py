"""
clarify:
nums - positive integers
target - positive integer
return - minimal length of a subarray whose sum is greater than or equal to target, else 0
in other words, we want to find the shortest subarray whose numbers add up to a number greater than or equal to target
seems like sliding window would be a candidate

input:
nums - positive integers
target - positive integer

output:
return - minimal length of a subarray whose sum is greater than or equal to target, else 0

edge case:
maybe, input is length 1
sum of subarray is equal
sum of subarray is greater

strategy:
let's say we use sliding window
the end of the window could expand on each iteration
when would start advance?
well, on a side note, on each iteration, we can check to see if we eneed to update the length of the smallest subarray. we would perform that update only if the sum of the subarray is greater than or equal to target
again - back to when to shrink the window
well, we want to expand the window while the sum is less than target
so let's advance start only while advancing start would not make the sum of numbers in the window less than target
and, also, how do we keep track of shortest length? just an int variable

test:
target = 3
input = [1, 2, 3]
window = [1]
window = [1, 2]
window = [1, 2, 3]
now we advance start
window = [2, 3]
shortest = 2

let's see what we've got
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        sub_sum = 0 # sum of current subarray
        res = float('inf')
        for end in range(len(nums)):
            end_int = nums[end]
            sub_sum += end_int
            # shrink window
            while sub_sum - nums[start] >= target:
                sub_sum -= nums[start]
                start += 1
            # conditionally update
            if sub_sum >= target:
                res = min(res, end - start + 1)
        return 0 if res == float('inf') else res


        
