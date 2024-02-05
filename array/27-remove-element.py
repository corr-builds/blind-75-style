"""
clarify:
remove all val in place
nums order may change
if first k els of array not equal to val, array must have k els first

input:
nums - int array
val - int

output:
num of els in nums not equal to val

edge case:
all nums equal to val
length 0

strategy:
hmm, could you use swappoing?
eg
[1, 2, 5, 2, 3], val = 2
swap 1 and 2 if second is val so val appears second
2 and 5
val appears first, so swap
2 and 2
hmm
that doesn't work
well, another way
a fast reader pointer and a slow writer pointer
basically reader goes fast
and we write what is at reader only if it does not equal val
if reader equals to val, we essentially continue until reader does not equal val

test:
[1, 2, 5, 2, 2, 3], val = 2
r = 1
w = 1
write 1
r = 2
skip
r = 5
write 5
r = 2
skip
r = 2
skip
r = 3
write 3

"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        reader = writer = 0
        for reader in range(len(nums)):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
        return writer
        
