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
        if not head:
            return None
        # put nodes in stack
        stack = []
        left = head
        while left:
            stack.append(left)
            left = left.next

        """while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        """


        # re-arrange pointers in spiral fashion
        left = head
        right = stack.pop()
        print(stack)
        while left != right:
            left.next = right
            print("connect " + str(left) + " to " + str(right))
            left = left.next
            print("connect " + str(right) + " to " + str(left))
            right.next = left

            right = stack.pop()

        left.next = None # important step - when they meet, connect the middle of the spiral to null since it's the new end
        return head

        
