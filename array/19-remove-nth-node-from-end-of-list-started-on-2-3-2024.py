"""
clarify:
remove the nth node from the end

input:
head node of linked list , n

output:
head node of linked list

edge case:
size 1
the node we are removing is at the end

strategy:
the removal: say we remove 4, as in the image
we need one pointer at 3 and one pointer at 5 (immediately before and immediately after)
that way we tie them back together

ohh actually I realized we are removing the nth node from the end, not the nth node from the front
hmm
so how about we traverse until we find the end, storing the nodes in a stack
then we pop of until we are at the nth node from the end
at that point, to do the removal, we need access to the node immediately before and immediately after
the one we are going to remove
the next one in the stack will be the node immediately before
and we can trail, when we start popping, with a pointer that has an offset of 1 (immediately behind)
to get the node immediately after


test:
n = 2
[1, 2, 3]
stack = [1, 2, 3]
start to traverse back
pop 3
pop 2
add trailing pointer at 3
pop 1, now connect 1 and 3 and delete 2
n = 1
[1]
stack = [1]
start to traverse back
pop 1
trailing pointer is at 1 + the end index, so assume that is null
there is nothing left to pop from the stack, so assume the previous is null, too
connect the nulls, also setting head as null < ??? come back to how to handle this <- about this case - remember to set the head pointer iff we ... change the head ... aka if we remove the element at the front of the list
return []

I should have started from the top by specifying my cases. Cases:
size is 1 (covered from the first if)
remove from the middle - regular
remove rom the end - left.next = left.next.next (None)
remove from the front - simply set head as right

now i'll try another approach - 2 pointer. let's say i traverse from the end, then use math (len - distance from end) to traverse again from theh end and perform the removal

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        traverser = head
        length = 1
        # traverse to the end
        while traverser.next:
            length += 1
            traverser = traverser.next
        # traverse to right before the node we want to delete

        dist = length - n # get distance from start of node to delete. so for [1] and n = 1, we want to remove node at 0. this makes it effectively 0-indexed

        # edge case where you are removing head
        if dist == 0:
            return head.next

        # perform removal
        i = 1
        traverser = head
        while i < dist: # trav to node before node we want to remove
            i += 1
            traverser = traverser.next

        traverser.next = None if not traverser.next else traverser.next.next # removal

        return head
        
