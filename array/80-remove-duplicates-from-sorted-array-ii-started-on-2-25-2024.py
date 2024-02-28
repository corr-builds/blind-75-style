"""
clarify:
remove duplicates in place so duplicates appear at most twice

input:
nums - int array in increasing order

output:
k, where k is the last idx of the new array (result placed in first k slots of nums)

edge case:
len of nums is 1 or 2
all numbers are the same
count of each number is already 2

strategy:
cases
[2, 2, 2 - if the next 2 are equal and the third is different, continue. if the third is the same, write the next distinct value
2, 2, 2 - same as above
2, 2, 2] - same as above - i'll just need to leave enough space for my pointers to traverse to the end
pointers
slow writer pointer
fast reader pointer
end iteration when fast reaches end and return slow

test:
[1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
f = 1
s = 0
f - s is 1, so iterate, moving f
f = 2
f - s = 2 and the values at f and s are equal, so continue to move f until the value at f does not equal the value at s. once this is true, write the value at f to where s is
f = 3
[1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
f - s = 2 still, but since the values at s and f are different, it is valid
also, after we write, we should make s equal to f - 1
s = 2
now f = s, but f-s = 1, so it is okay
iterate, moving f.
f = 4
val at f = val at s and f-s = 2, so now move f until val at f does not equal val at s
f = 7 (first 3)
now vals at f and s are different. write val at f to val at s + 1. note - the condition should be that they are not equal AND that val at f is greater than val at s
[1, 1, 2, 2, 3, 2, 2, 3, 3, 3]
now keep progressing until end. and actually, about the s pointer, i could probably keep it at the next write position instead of at the first position of each distinct number series



stopping this play by play, let's notice something. say we start s at 0 still and start f at 2. what if we move f by 2 at a time?
the reason being that
[1, 1, 1, 2, 3, 3, 3]
s = 0, f = 2. values are same, so move f until values are different
now f = 3. values are different, so write val at f to val at s
[1, 1, 2, 2, 3, 3, 3]
now that we have done a write, we can move f by 2.
f = 5
values at f and s are different, and that's fine
stopping this play out. i'm trying to optimize too early

back to the drawing board. let's test with this: [1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5]
                                                  0  1. 2. 3. 4. 5. 6. 7. 8. 0 10 11
a general idea of strategy before walking thru: have a slow writer and a fast reader
keep slow writer at next potential write position
keep fast reader at next possible number that needs to be written
so start with
s

todo - when resume, watch video solution and understand

new strategy:
for a sequence of the same number, traverse f to the end, counting
traverse s to either 1 or 2 depending on the count, writing the value at f to s
bump f up so that it starts with the next sequence on the next iteration
s always ends up in its next potential write position (after the end of the newly written number series)
at the end, return s

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = f = 0

        while f < len(nums):
            count = 1

            # move f, reading
            while f < len(nums) - 1 and nums[f] == nums[f + 1]:
                f += 1
                count += 1

            # move s, writing
            count = min(2, count) # 2 or 1
            while count > 0:
                count -= 1
                nums[s] = nums[f]
                s += 1

            f += 1

        return s

        
