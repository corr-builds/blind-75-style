"""
clarify:
I clarified below

input:
nums - array of 0s and 1s

output:
max # of consecutive 1s IF you can flip at most 1 0
so you can flip 0 0s or 1 0
that means your max connsecutive ones will consist of all 1s
or of all 1s except for 1 0
so if you represent that in a hash table
that means 1s with any count
and 0s with count 0 or 1
variable length window

edge case:
all 1s or all 0s
only 1 0 to flip

strategy:
sliding window variable length

test:
[1, 0, 1, 0, 1, 1]
ht = {1:1}
ht = {1:1, 0:1}
ht = {1:2, 0:1}
ht = {1:2, 0:2}
invalid, so move left pointer til valid
ht = {1:1, 0:2}
ht = {1:1, 0:1}
valid
and so on until
ht = {1:3, 0:1}

let's try it

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        zeroes = 0
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
        
