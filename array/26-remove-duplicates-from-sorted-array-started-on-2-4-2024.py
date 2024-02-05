"""
clarify:
size of nums does not matter

input:
nums - sorted in increasing order

output:
remove duplicates
return the number of unique elements in nums

edge case:
consider using two pointer
let's say we have a writer pointer and a reader pointer
writer writes the number
reader reads
so writer can move exactly once ebery iteratiion, writing when reader indicates so
before that, reader can move until the next number is not a duplicate. then it will tell writer to write that number
stop iterating once reader is at the last index

strategy:
getting some issues... how about we handle this differently with reader as fast poipnter and writer as slow pointer. so we loop always for the fast pointer and only act on the slow pointer in case of some condition

test:

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = reader = 1
        while reader < len(nums):
            if nums[reader] != nums[reader - 1]:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1
        return writer
        
