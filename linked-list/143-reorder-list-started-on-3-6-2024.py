"""
clarify:
we can think of this as two lists in opposite orders, interlaced
consider that we divide the list in half
right half - sort in opposite order
left half - keep in original order
then, for the final list, interlace the two, picking from one list then the other, starting with left

how does the ll data structure affect this?
well, we can already read left list in order by starting from the beginning
how could we read "right" list in opposite order? I guess we'd have to reverse the right half of the list

to reverse?
we'd need to make the "next" pointers of each node actually point to the previous node

so maybe we do something like
iterate thru the list once to get length
reverse "right" half of list, where that is 1/2 of length, or in case of odd number, 1/2 - 1
now interlace

hmm, actually, now that I'm drawing things, they seem different

<see drawing>

What is the pattern in this drawing?
The pattern is something that might be able to be solved by having two pointers starting from the ends and closing in
Let’s call them left and right

Describing the drawing in pointers:
Left points to right
Move left
Right points to left
Move right
Left points to right
Move left
Right points to left
Move right
Right and left have met, so we can end iteration

Question is, given constraints of linked list, how to traverse right in this fashion?
We’d have to reverse the right half of the linked list. But to do that, we’d need to know the half way point, which means we need the length, which means we need another iteration
Instead, let’s just traverse all the way once and use a stack

input:

output:

edge case:

strategy:

test:

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the midpoint
        slow, fast = head, head.next
        # odd - s f x, x s x (f is at null) <- so slow.next will be start of second half
        # even - s f x x, x s x f <- so slow.next will be start of second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of list
        secondhead = slow.next # create head for second list
        slow.next = None # make tail of left list none
        prev = None
        cur = secondhead
        while cur:
            orig_cur_next = cur.next # temp variable
            cur.next = prev # reverse link
            prev = cur
            cur = orig_cur_next

        # interlace
        secondcur = prev
        firstcur = head
        while secondcur: # while secondcur works because second list will be same length or shorter, and we want to stop when one of them is null
            tmpfirst, tmpsecond = firstcur.next, secondcur.next # store copies of the current next links on either list (L1 and Ln-1, initially)
            firstcur.next = secondcur # make item from first point to item from second
            secondcur.next = tmpfirst # make item now pointed to from second list point to next item from first list (which we preserve using a temp variable)
            firstcur, secondcur = tmpfirst, tmpsecond # advance to next items in list
        # we can kind of think of the above logic as working on two "links" per iteration. link a to b, link b to c. repeat

        return head

        
