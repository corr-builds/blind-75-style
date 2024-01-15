"""
clarify:
capacity of nums1 is size of nums1 + nums2

input:
nums1 and nums2 - int arrays, sorted in increasing order

output:
elements in nums1 and nums2 in single array sorted in increasing order ARE STORED IN nums1

edge case:
all equal

strategy:
obviously 2 pointer, choose whichever is smaller
the challenge is in scooting
if we select something from nums2
so nums2 = 2
and nums1 = 0, 4, 0
okay basically if we select something from nums2, shift every element in nums1 at that spot and after to the right by 1
is there a better way than shifting?
so imagine the given example
lets say pointers are a and b
a at 1
b at 2
leave in place and advance a
a at 2
b at 2
leave in place ad advance a
a at 3
b at 2
shift everything in nums1 down
advance b
NEW NOTES
does this work if nums2 is empty? nums2 can be empty - maybe we could just handle those edge cases separately? - actually - if nums1 or nums2 is empty, then it's already sorted


test:
did so above

"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a, b = 0, 0
        temp = list()
        while a < m and b < n:
            if nums1[a] < nums2[b]:
                temp.append(nums1[a])
                a += 1
            else:
                temp.append(nums2[b])
                b += 1
        while a < m:
            temp.append(nums1[a])
            a += 1
        while b < n:
            temp.append(nums2[b])
            b += 1
        nums1[:] = temp[:]
        return
        
